#!/usr/bin/env python3
"""Consolidate per-batch screening results into a single deduplicated accepted set.

Merges data/snowballing/screened/accepted_*.json, removes duplicates (within the
accepted set and against the existing collaborative-perception.bib), and reports the
taxonomy distribution. Flags borderline papers (communication/edge/federated/attack
heavy) for a uniform second-pass review.
"""
import json
import re
import glob
from pathlib import Path

import bibtexparser

ROOT = Path(__file__).resolve().parent.parent.parent
BORDERLINE = re.compile(
    r"federat|jamming|interfere|resource alloc|spectrum|semantic communicat|"
    r"compress|sampling|tamper|attack|networking|edge-assisted|edge-enabled",
    re.I,
)


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main() -> None:
    db = bibtexparser.load(open(ROOT / "collaborative-perception.bib"))
    existing = {norm(e.get("title", "")) for e in db.entries}

    seen: set = set()
    merged = []
    for f in sorted(glob.glob(str(ROOT / "data/snowballing/screened/accepted_*.json"))):
        data = json.load(open(f))
        for p in data.get("accepted", []):
            key = norm(p.get("title", ""))
            if not key or key in seen or key in existing:
                continue
            seen.add(key)
            p["borderline"] = bool(BORDERLINE.search(p.get("title", "")))
            merged.append(p)

    out = ROOT / "data/snowballing/accepted_consolidated.json"
    json.dump(merged, open(out, "w"), indent=1, ensure_ascii=False)

    from collections import Counter
    print(f"merged unique accepted (deduped vs bib): {len(merged)}")
    print("borderline flagged:", sum(1 for p in merged if p["borderline"]))
    print("by modality:", Counter(p.get("modality") for p in merged))
    print("by collaboration:", Counter(p.get("collaboration") for p in merged))
    print("by year:", dict(sorted(Counter(p.get("year") for p in merged).items(),
                                   key=lambda x: (x[0] is None, x[0]))))
    print("wrote", out)


if __name__ == "__main__":
    main()
