#!/usr/bin/env python3
"""Enrich kept snowballing papers with DOI / URL via Semantic Scholar title search.

The forward-snowballing step captured title/authors/year/venue/abstract but not
identifiers, so paper links are missing. This queries the Semantic Scholar paper
search endpoint by title to recover externalIds.DOI / ArXiv / openAccessPdf / url.
"""
import json
import logging
import re
import time
from pathlib import Path
from typing import Any, Dict, List

import requests

ROOT = Path(__file__).resolve().parent.parent.parent
API = "https://api.semanticscholar.org/graph/v1/paper/search"

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def enrich(papers: List[Dict[str, Any]], delay: float = 1.1) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for i, p in enumerate(papers, 1):
        title = p["title"]
        doi, arxiv, url = "", "", ""
        try:
            r = requests.get(API, params={"query": title, "limit": 3,
                                          "fields": "title,externalIds,openAccessPdf,url"},
                             timeout=30, headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code == 200:
                for cand in r.json().get("data", []):
                    if norm(cand.get("title", "")) == norm(title):
                        ext = cand.get("externalIds") or {}
                        doi = ext.get("DOI", "") or ""
                        arxiv = ext.get("ArXiv", "") or ""
                        oa = cand.get("openAccessPdf") or {}
                        url = oa.get("url", "") or cand.get("url", "") or ""
                        break
        except requests.RequestException as e:
            logger.warning("  [%d] Semantic Scholar error: %s", i, e)
        p2 = dict(p)
        p2["doi"], p2["arxiv"], p2["url"] = doi, arxiv, url
        out.append(p2)
        kind = "DOI" if doi else ("arXiv" if arxiv else ("url" if url else "NONE"))
        logger.info("[%d/%d] %s: %s", i, len(papers), kind, title[:55])
        time.sleep(delay)
    return out


def main() -> None:
    with open(ROOT / "data/snowballing/kept_final.json", encoding="utf-8") as f:
        papers = json.load(f)
    enriched = enrich(papers)
    out = ROOT / "data/snowballing/kept_enriched.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(enriched, f, indent=1, ensure_ascii=False)
    n = sum(1 for p in enriched if p["doi"] or p["arxiv"] or p["url"])
    logger.info("enriched %d papers; %d got a link (%d none)", len(enriched), n, len(enriched) - n)
    logger.info("wrote %s", out)


if __name__ == "__main__":
    main()
