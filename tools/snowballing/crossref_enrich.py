#!/usr/bin/env python3
"""Recover missing DOIs for kept snowballing papers via the Crossref REST API.

Reads ``data/snowballing/kept_enriched.json``, and for every paper that still lacks a
``doi``/``arxiv`` identifier, queries Crossref by bibliographic title and accepts the top
match whose title is sufficiently similar (Jaccard token overlap >= ``SIM_THRESHOLD``).
The file is updated in place.

Crossref asks API users to identify themselves with a contact ``mailto``. Set it via the
``CROSSREF_MAILTO`` environment variable; a neutral project address is used as a fallback.
"""
import concurrent.futures as cf
import json
import logging
import os
import re
from pathlib import Path
from typing import Any, Dict, List

import requests

ROOT = Path(__file__).resolve().parent.parent.parent
KEPT = ROOT / "data" / "snowballing" / "kept_enriched.json"
MAILTO = os.getenv("CROSSREF_MAILTO", "awesome-cp@users.noreply.github.com")
SIM_THRESHOLD = 0.75
MAX_WORKERS = 6
RETRIES = 3

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def _tokens(s: str) -> List[str]:
    return re.sub(r"[^a-z0-9]", " ", (s or "").lower()).split()


def _similarity(a: str, b: str) -> float:
    """Jaccard token-overlap similarity between two titles."""
    ta, tb = set(_tokens(a)), set(_tokens(b))
    return len(ta & tb) / max(1, len(ta | tb))


def recover_doi(paper: Dict[str, Any]) -> Dict[str, Any]:
    """Fill ``paper['doi']`` from Crossref if it has no identifier yet (retried)."""
    if paper.get("doi") or paper.get("arxiv"):
        return paper
    title = paper.get("title", "")
    if not title:
        return paper
    params = {"query.bibliographic": title, "rows": 2, "mailto": MAILTO}
    headers = {"User-Agent": f"awesome-cp/1.0 (mailto:{MAILTO})"}
    for attempt in range(1, RETRIES + 1):
        try:
            r = requests.get("https://api.crossref.org/works", params=params,
                             timeout=30, headers=headers)
            if r.status_code == 200:
                for item in r.json().get("message", {}).get("items", []):
                    cand = " ".join(item.get("title", []) or [])
                    if cand and _similarity(title, cand) >= SIM_THRESHOLD:
                        paper["doi"] = item.get("DOI", "") or paper.get("doi", "")
                        break
                return paper
            if r.status_code in (429, 500, 502, 503):       # transient: retry
                continue
            return paper
        except requests.RequestException as e:
            logger.warning("  [%d/%d] Crossref error for %r: %s", attempt, RETRIES, title[:50], e)
    return paper


def main() -> None:
    with open(KEPT, "r", encoding="utf-8") as f:
        papers: List[Dict[str, Any]] = json.load(f)

    missing = [p for p in papers if not (p.get("doi") or p.get("arxiv"))]
    logger.info("querying Crossref for %d papers (mailto=%s)", len(missing), MAILTO)
    with cf.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        list(ex.map(recover_doi, missing))   # recover_doi mutates dicts in place

    n_id = sum(1 for p in papers if p.get("doi") or p.get("arxiv"))
    with open(KEPT, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=1, ensure_ascii=False)
    logger.info("now with a real identifier: %d / %d", n_id, len(papers))


if __name__ == "__main__":
    main()
