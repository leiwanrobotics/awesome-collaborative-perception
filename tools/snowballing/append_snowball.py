#!/usr/bin/env python3
"""Append forward-snowballing kept papers to collaborative-perception.bib.

Reads data/snowballing/kept_enriched.json (kept papers + recovered doi/arxiv/url),
normalises taxonomy labels to the repo's CP- keyword scheme, tags every entry with
CP-Snowball, and appends well-formed BibTeX entries to the bib file.
"""
import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, Set

import bibtexparser

ROOT = Path(__file__).resolve().parent.parent.parent
BIB = ROOT / "collaborative-perception.bib"

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# Common LaTeX accent commands -> Unicode, so author names survive de-bracing
# (e.g. "Fr{\"o}hlich" -> "Fröhlich" rather than "Frhlich").
_ACCENTS = {
    r'\"o': "ö", r'\"a': "ä", r'\"u': "ü", r'\"O': "Ö", r'\"A': "Ä", r'\"U': "Ü",
    r"\'e": "é", r"\'a": "á", r"\'o": "ó", r"\'i": "í", r"\'c": "ć", r"\'n": "ń",
    r"\`e": "è", r"\`a": "à", r"\^o": "ô", r"\^e": "ê", r"\^a": "â", r"\~n": "ñ",
    r"\~a": "ã", r"\c{c}": "ç", r"\v{s}": "š", r"\v{c}": "č", r"\ss": "ß",
}

TASK_KW = {
    "Object Detection": "CP-Object Detection",
    "Semantic Segmentation": "CP-Semantic Segmentation",
    "Object Tracking": "CP-Object Tracking",
    "Motion Prediction": "CP-Motion Prediction",
    "Motion/Trajectory Prediction": "CP-Motion Prediction",
    "Trajectory Prediction": "CP-Motion Prediction",
    "Lane Detection": "CP-Lane Detection",
    "Multi-Task & Task-Agnostic": "CP-Task-agnostic",
    "Multi-Task and Task-Agnostic": "CP-Task-agnostic",
    "Occupancy": "CP-Task-agnostic",
    "Scene Completion": "CP-Task-agnostic",
    "Dataset / Benchmark": "CP-Dataset",
    "Dataset": "CP-Dataset",
    "Benchmark": "CP-Dataset",
}
JOURNAL_RE = re.compile(r"transactions|journal|letters|access|sensors|magazine|\bIEEE [A-Z]", re.I)


def slug(title: str, year: Any, used: Set[str]) -> str:
    words = re.findall(r"[A-Za-z0-9]+", title)[:4]
    base = "Snowball" + str(year) + "".join(w.capitalize() for w in words)[:40]
    key = base
    i = 2
    while key in used:
        key = f"{base}{i}"
        i += 1
    used.add(key)
    return key


def venue_field(venue: str) -> str:
    return "journal" if JOURNAL_RE.search(venue or "") else "booktitle"


def keywords_for(p: Dict[str, Any]) -> str:
    kws = ["CP-Snowball"]
    mod = p.get("modality")
    if mod == "LiDAR":
        kws.append("CP-LiDAR")
    elif mod == "Camera":
        kws.append("CP-Camera")
    elif mod == "LiDAR-Camera":
        kws += ["CP-LiDAR", "CP-Camera"]
    collab = p.get("collaboration")
    if collab in ("Early", "Intermediate", "Late", "Hybrid"):
        kws.append("CP-" + collab)
    for t in p.get("tasks", []):
        kw = TASK_KW.get(t)
        if kw and kw not in kws:
            kws.append(kw)
    if not any(k.startswith("CP-Object") or k.startswith("CP-Semantic") or k.startswith("CP-Lane")
               or k.startswith("CP-Motion") or k == "CP-Task-agnostic" or k == "CP-Dataset"
               for k in kws):
        kws.append("CP-Object Detection")  # default task
    return ", ".join(kws)


def esc(s: str) -> str:
    """Plain-text a BibTeX field: resolve common accents, then drop residual braces."""
    s = s or ""
    for tex, uni in _ACCENTS.items():
        s = s.replace(tex, uni).replace("{" + tex + "}", uni)
    return s.replace("{", "").replace("}", "").replace("\\", "").strip()


def main() -> None:
    with open(ROOT / "data/snowballing/kept_enriched.json", encoding="utf-8") as f:
        papers = json.load(f)
    with open(BIB, encoding="utf-8") as f:
        db = bibtexparser.load(f)
    used: Set[str] = {e["ID"] for e in db.entries}

    blocks = []
    for p in papers:
        key = slug(p["title"], p.get("year", ""), used)
        venue = esc(p.get("venue", ""))
        vfield = venue_field(venue)
        authors = " and ".join(esc(a) for a in p.get("authors", []) if a) or "Unknown"
        lines = [f"@article{{{key}," if vfield == "journal" else f"@inproceedings{{{key},"]
        lines.append(f"  title = {{{esc(p['title'])}}},")
        lines.append(f"  author = {{{authors}}},")
        if p.get("year"):
            lines.append(f"  year = {{{p['year']}}},")
        if venue:
            lines.append(f"  {vfield} = {{{venue}}},")
        if p.get("doi"):
            lines.append(f"  doi = {{{p['doi']}}},")
        if p.get("arxiv"):
            lines.append(f"  eprint = {{{p['arxiv']}}},")
        if p.get("url") and not p.get("doi") and not p.get("arxiv"):
            lines.append(f"  url = {{{p['url']}}},")
        lines.append(f"  keywords = {{{keywords_for(p)}}},")
        lines.append("}")
        blocks.append("\n".join(lines))

    with open(BIB, "a", encoding="utf-8") as f:
        f.write("\n\n" + "\n\n".join(blocks) + "\n")
    logger.info("appended %d snowball entries to %s", len(blocks), BIB)


if __name__ == "__main__":
    main()
