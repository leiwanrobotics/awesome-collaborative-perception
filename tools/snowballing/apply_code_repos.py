#!/usr/bin/env python3
"""Apply discovered code repositories to collaborative-perception.bib.

Reads ``data/snowballing/code_candidates.json`` (produced by find_code_repos.py) and
inserts a ``code = {url}`` field into each matching BibTeX entry that does not already
have one. By default only VERIFIED matches (README-confirmed) are applied; pass
``--also-keys k1,k2`` to additionally apply specific reviewed citation keys.

Usage:
    python tools/snowballing/apply_code_repos.py [--dry-run] [--also-keys KEY,KEY]
"""
import argparse
import json
import logging
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent.parent.parent
BIB = ROOT / "collaborative-perception.bib"
CAND = ROOT / "data" / "snowballing" / "code_candidates.json"

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def load_targets(also_keys: List[str], from_list: str) -> Dict[str, str]:
    """citation_key -> code url, from VERIFIED candidates plus any --also-keys.

    With --from-list, instead read a plain ``[{"key","repo"}]`` JSON file (used for
    the web-search-sourced, independently re-verified matches).
    """
    if from_list:
        items = json.loads(Path(from_list).read_text(encoding="utf-8"))
        return {it["key"]: it["repo"] for it in items if it.get("repo")}
    data = json.loads(CAND.read_text(encoding="utf-8"))
    extra = {k.strip() for k in also_keys if k.strip()}
    targets: Dict[str, str] = {}
    for c in data["candidates"]:
        url = (c.get("best") or {}).get("url", "")
        if not url:
            continue
        if c["confidence"] == "VERIFIED" or c["citation_key"] in extra:
            targets[c["citation_key"]] = url
    return targets


def apply(targets: Dict[str, str], dry_run: bool) -> None:
    lines = BIB.read_text(encoding="utf-8").splitlines(keepends=True)
    header = re.compile(r"^@\w+\{([^,]+),")
    field = re.compile(r"^\s*([A-Za-z]+)\s*=")
    out: List[str] = []
    applied = skipped = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = header.match(line)
        if not m or m.group(1) not in targets:
            i += 1
            continue
        key = m.group(1)
        # Collect this entry's field lines to decide placement / detect existing code.
        j = i + 1
        has_code = False
        insert_at = len(out)  # default: right after the header
        placed = False
        while j < len(lines) and not header.match(lines[j]):
            fm = field.match(lines[j])
            if fm:
                name = fm.group(1).lower()
                if name == "code":
                    has_code = True
                if not placed and name > "code":
                    insert_at = len(out) + (j - (i + 1))
                    placed = True
            out.append(lines[j])
            j += 1
        if has_code:
            skipped += 1
        else:
            out.insert(insert_at, f"  code = {{{targets[key]}}},\n")
            applied += 1
            logger.info("  + %-46.46s %s", key, targets[key])
        i = j

    logger.info("\nApplied %d, skipped %d (already had code). Targets: %d",
                applied, skipped, len(targets))
    if dry_run:
        logger.info("[dry-run] bib not written.")
        return
    BIB.write_text("".join(out), encoding="utf-8")
    logger.info("Wrote %s", BIB.relative_to(ROOT))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--also-keys", default="", help="comma-separated citation keys to also apply")
    parser.add_argument("--from-list", default="", help="JSON file of [{key,repo}] to apply instead")
    args = parser.parse_args()
    targets = load_targets(args.also_keys.split(","), args.from_list)
    apply(targets, args.dry_run)


if __name__ == "__main__":
    main()
