#!/usr/bin/env python3
"""Add standardized realistic-issue keywords to bib entries from FINAL_labels.json.

Edits each entry's ``keywords = {...}`` line textually (preserving the rest of the
file byte-for-byte) so the diff stays reviewable. Idempotent: tags already present
are not duplicated.
"""

import json
import re
import sys
from pathlib import Path

ISSUE_TAG = {
    "pose": "CP-Pose-Error",
    "latency": "CP-Latency",
    "comm": "CP-Comm-Efficiency",
    "commrobust": "CP-Comm-Robust",
    "domain": "CP-Domain-Gap",
    "hetero": "CP-Heterogeneous",
    "adversarial": "CP-Adversarial",
}

BIB = Path("collaborative-perception.bib")
LABELS = Path("plan/cp_classify/FINAL_labels.json")


def main() -> None:
    dry = "--dry-run" in sys.argv
    labels = json.loads(LABELS.read_text())
    text = BIB.read_text()

    # Split into entries keeping the leading "@type{key,". Each entry starts at a
    # line beginning with '@'.
    parts = re.split(r"(?m)^(?=@)", text)
    out, changed = [], 0
    for block in parts:
        m = re.match(r"@\w+\{([^,]+),", block)
        if not m:
            out.append(block)
            continue
        key = m.group(1).strip()
        tags = [ISSUE_TAG[c] for c in labels.get(key, [])]
        if not tags:
            out.append(block)
            continue
        km = re.search(r"(keywords\s*=\s*\{)([^}]*)(\})", block)
        if not km:
            out.append(block)
            continue
        existing = [t.strip() for t in km.group(2).split(",") if t.strip()]
        add = [t for t in tags if t not in existing]
        if not add:
            out.append(block)
            continue
        new_kw = km.group(1) + ", ".join(existing + add) + km.group(3)
        block = block[: km.start()] + new_kw + block[km.end():]
        out.append(block)
        changed += 1

    new_text = "".join(out)
    print(f"entries updated: {changed}")
    if dry:
        print("(dry-run; no write)")
        return
    BIB.write_text(new_text)
    print(f"wrote {BIB}")


if __name__ == "__main__":
    main()
