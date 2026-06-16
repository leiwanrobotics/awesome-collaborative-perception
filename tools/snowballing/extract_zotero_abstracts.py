#!/usr/bin/env python3
"""Extract first-page text (title + abstract) for every paper in a Zotero
collection, using the local Zotero 7 HTTP API plus the on-disk PDF / full-text
cache.

Used to give the realistic-issue classifier real abstracts to read, since the
forward-snowballing bib entries are title-only.

Output: a JSON list of {zkey, title, date, doi, pdf, text} written to ``--out``.
"""

import json
import logging
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

API = "http://127.0.0.1:23119/api/users/11769416"
STORAGE = Path.home() / "Zotero" / "storage"
COLLECTION = "A7FNP8EV"  # 01-CP / 01-from-2024
MAX_CHARS = 4000


def api_get(path: str) -> list:
    with urllib.request.urlopen(f"{API}{path}", timeout=20) as r:
        return json.load(r)


def collection_items(key: str) -> list:
    items, start = [], 0
    while True:
        batch = api_get(f"/collections/{key}/items/top?limit=100&start={start}")
        if not batch:
            break
        items.extend(batch)
        if len(batch) < 100:
            break
        start += 100
    return items


def pdf_text(att_key: str, filename: str) -> str:
    """Return extracted text: prefer the Zotero full-text cache, else pdftotext."""
    folder = STORAGE / att_key
    cache = folder / ".zotero-ft-cache"
    if cache.exists():
        txt = cache.read_text(errors="ignore")
        if txt.strip():
            return txt[:MAX_CHARS]
    pdf = folder / filename
    if pdf.exists():
        try:
            out = subprocess.run(
                ["pdftotext", "-f", "1", "-l", "2", str(pdf), "-"],
                capture_output=True, text=True, timeout=30,
            )
            return out.stdout[:MAX_CHARS]
        except (subprocess.SubprocessError, OSError) as e:
            logger.warning("pdftotext failed for %s: %s", att_key, e)
    return ""


def process(item: dict) -> dict:
    dd = item["data"]
    key = dd["key"]
    rec = {
        "zkey": key,
        "title": dd.get("title", ""),
        "date": dd.get("date", ""),
        "doi": dd.get("DOI", ""),
        "pdf": "",
        "text": "",
        "abstract_meta": dd.get("abstractNote", ""),
    }
    try:
        children = api_get(f"/items/{key}/children")
    except Exception as e:  # noqa: BLE001 - localhost API, log and continue
        logger.warning("children fetch failed for %s: %s", key, e)
        return rec
    for c in children:
        cd = c["data"]
        if cd.get("itemType") == "attachment" and cd.get("contentType") == "application/pdf":
            rec["pdf"] = cd.get("filename", "")
            rec["text"] = pdf_text(cd["key"], cd.get("filename", ""))
            break
    return rec


def main() -> None:
    out_path = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv \
        else Path("plan/zotero_from2024.json")
    items = collection_items(COLLECTION)
    logger.info("collection items: %d", len(items))
    with ThreadPoolExecutor(max_workers=8) as ex:
        recs = list(ex.map(process, items))
    with_text = sum(1 for r in recs if r["text"].strip())
    logger.info("records with extracted text: %d / %d", with_text, len(recs))
    out_path.write_text(json.dumps(recs, ensure_ascii=False, indent=2))
    logger.info("wrote %s", out_path)


if __name__ == "__main__":
    main()
