#!/usr/bin/env python3
"""Enrich kept snowballing papers with DOI / URL via Semantic Scholar title search.

The forward-snowballing step captured title/authors/year/venue/abstract but not
identifiers, so paper links are missing. This queries the Semantic Scholar paper
search endpoint by title to recover externalIds.DOI / ArXiv / openAccessPdf / url.
"""
import json
import time
import re
import sys
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent.parent
API = "https://api.semanticscholar.org/graph/v1/paper/search"


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def enrich(papers, delay=1.1):
    out = []
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
        except Exception as e:
            print(f"  [{i}] error: {e}", file=sys.stderr)
        p2 = dict(p)
        p2["doi"], p2["arxiv"], p2["url"] = doi, arxiv, url
        out.append(p2)
        print(f"[{i}/{len(papers)}] {'DOI' if doi else ('arXiv' if arxiv else ('url' if url else 'NONE'))}: {title[:55]}")
        time.sleep(delay)
    return out


def main():
    papers = json.load(open(ROOT / "data/snowballing/kept_final.json"))
    enriched = enrich(papers)
    out = ROOT / "data/snowballing/kept_enriched.json"
    json.dump(enriched, open(out, "w"), indent=1, ensure_ascii=False)
    n = sum(1 for p in enriched if p["doi"] or p["arxiv"] or p["url"])
    print(f"\nenriched {len(enriched)} papers; {n} got a link ({len(enriched)-n} none)")
    print("wrote", out)


if __name__ == "__main__":
    main()
