#!/usr/bin/env python3
"""Consolidate per-batch screening results into a single deduplicated accepted set.

Merges data/snowballing/screened/accepted_*.json, removes duplicates (within the
accepted set and against the existing collaborative-perception.bib), and reports the
taxonomy distribution. Flags borderline papers (communication/edge/federated/attack
heavy) for a uniform second-pass review.
"""
import glob
import json
import logging
import re
from collections import Counter
from pathlib import Path

import bibtexparser

ROOT = Path(__file__).resolve().parent.parent.parent

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)
BORDERLINE = re.compile(
    r"federat|jamming|interfere|resource alloc|spectrum|semantic communicat|"
    r"compress|sampling|tamper|attack|networking|edge-assisted|edge-enabled",
    re.I,
)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main() -> None:
    with open(ROOT / "collaborative-perception.bib", encoding="utf-8") as f:
        db = bibtexparser.load(f)
    existing = {norm(e.get("title", "")) for e in db.entries}

    seen: set = set()
    merged = []
    for path in sorted(glob.glob(str(ROOT / "data/snowballing/screened/accepted_*.json"))):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        for p in data.get("accepted", []):
            key = norm(p.get("title", ""))
            if not key or key in seen or key in existing:
                continue
            seen.add(key)
            p["borderline"] = bool(BORDERLINE.search(p.get("title", "")))
            merged.append(p)

    out = ROOT / "data/snowballing/accepted_consolidated.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=1, ensure_ascii=False)

    logger.info("merged unique accepted (deduped vs bib): %d", len(merged))
    logger.info("borderline flagged: %d", sum(1 for p in merged if p["borderline"]))
    logger.info("by modality: %s", Counter(p.get("modality") for p in merged))
    logger.info("by collaboration: %s", Counter(p.get("collaboration") for p in merged))
    logger.info("by year: %s", dict(sorted(Counter(p.get("year") for p in merged).items(),
                                            key=lambda x: (x[0] is None, x[0]))))
    logger.info("wrote %s", out)


if __name__ == "__main__":
    main()
