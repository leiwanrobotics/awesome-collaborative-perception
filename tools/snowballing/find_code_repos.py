#!/usr/bin/env python3
"""Find official code repositories for papers that lack a code link.

Papers With Code was sunset (its API now redirects to Hugging Face), so this uses
GitHub repository search via the authenticated ``gh`` CLI. For every paper without a
code link it builds a query from the coined method name (when the title states one)
plus distinctive title words, searches GitHub, scores the candidates, and records the
best match with a confidence level. It never overwrites an existing link and writes
only a candidates file -- applying matches to the bib is a separate, reviewable step.

Output: ``data/snowballing/code_candidates.json``

Usage:
    python tools/snowballing/find_code_repos.py [--limit N] [--delay SECONDS]
"""
import argparse
import json
import logging
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "data_extraction"))
from make_category_timelines import first_author_etal, method_name  # noqa: E402
from readme_generator import ReadmeGenerator  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

DATA = ROOT / "data" / "categorized_papers.json"
OUT = ROOT / "data" / "snowballing" / "code_candidates.json"

_STOP = {
    "a", "an", "the", "for", "with", "via", "and", "of", "in", "on", "to", "from",
    "using", "based", "towards", "toward", "is", "are", "by", "into", "under", "over",
    "collaborative", "cooperative", "perception", "detection", "object", "multi",
    "agent", "vehicle", "autonomous", "driving", "network", "learning", "feature",
    "fusion", "3d", "scene", "point", "cloud", "lidar", "camera", "bev",
}


def content_tokens(title: str) -> List[str]:
    """Distinctive lowercase word tokens from a title (stopwords/generic terms dropped)."""
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9\-]+", title.lower())
    return [w for w in words if w not in _STOP and len(w) > 2]


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


# All-caps / generic tokens that method_name() may surface but that are too common to
# match a repo on (a repo merely containing "lidar" is not this paper's code).
METHOD_BLOCK = {
    "lidar", "radar", "camera", "image", "video", "rgb", "bev", "gps", "imu", "gnss",
    "3d", "2d", "4d", "ai", "ml", "dl", "iou", "map", "roi", "v2v", "v2i", "v2x",
}


def clean_method(title: str) -> Optional[str]:
    """method_name() with generic all-caps words filtered out."""
    m = method_name(title)
    if m and norm(m) in METHOD_BLOCK:
        return None
    return m


def build_query(title: str, method: Optional[str]) -> str:
    """A focused GitHub search string: method name (if any) + a few title keywords."""
    parts: List[str] = []
    if method:
        parts.append(method)
    for tok in content_tokens(title):
        if norm(tok) and norm(tok) not in {norm(p) for p in parts}:
            parts.append(tok)
        if len(parts) >= 4:
            break
    return " ".join(parts) or title[:60]


def gh_readme(full_name: str) -> str:
    """Raw README text of a repo via the gh CLI; '' on any failure."""
    try:
        proc = subprocess.run(
            ["gh", "api", f"/repos/{full_name}/readme",
             "-H", "Accept: application/vnd.github.raw+json"],
            capture_output=True, text=True, timeout=40, check=False,
        )
        return proc.stdout if proc.returncode == 0 else ""
    except subprocess.SubprocessError:
        return ""


def title_in_readme(title: str, readme: str) -> bool:
    """True if 5 consecutive title words appear verbatim in the README.

    Repos almost always quote their paper's title, and a contiguous 5-gram match is
    extremely unlikely by chance -- a precise confirmation that this repo is the
    paper's code rather than a coincidental keyword hit.
    """
    tw = re.findall(r"[a-z0-9]+", title.lower())
    rt = " ".join(re.findall(r"[a-z0-9]+", readme.lower()))
    if not rt:
        return False
    n = min(5, len(tw))
    if len(tw) < 5:
        return " ".join(tw) in rt
    return any(" ".join(tw[i:i + n]) in rt for i in range(len(tw) - n + 1))


def gh_search(query: str) -> List[Dict[str, Any]]:
    """GitHub repository search via the gh CLI; returns [] on any failure."""
    try:
        proc = subprocess.run(
            ["gh", "api", "-X", "GET", "/search/repositories",
             "-f", f"q={query}", "-F", "per_page=8"],
            capture_output=True, text=True, timeout=40, check=False,
        )
        if proc.returncode != 0:
            logger.warning("  gh search failed: %s", proc.stderr.strip()[:120])
            return []
        return json.loads(proc.stdout).get("items", [])
    except (subprocess.SubprocessError, json.JSONDecodeError) as exc:
        logger.warning("  gh search error: %s", exc)
        return []


def score_candidate(paper_title: str, method: Optional[str],
                    repo: Dict[str, Any]) -> Dict[str, Any]:
    """Score one repo against a paper. Returns dict with score + confidence."""
    name = repo.get("name", "") or ""
    full = repo.get("full_name", "") or ""
    desc = repo.get("description", "") or ""
    haystack = norm(name + " " + desc)

    title_toks = {norm(t) for t in content_tokens(paper_title)}
    title_toks.discard("")
    overlap = sum(1 for t in title_toks if t and t in haystack)
    overlap_ratio = overlap / max(1, len(title_toks))

    mnorm = norm(method) if method else ""
    acronym_in_name = bool(mnorm) and mnorm in norm(name)
    acronym_in_text = bool(mnorm) and mnorm in haystack

    score = 0.0
    if acronym_in_name:
        score += 5
    elif acronym_in_text:
        score += 2
    score += 2 * overlap + min(repo.get("stargazers_count", 0), 50) / 50.0
    if repo.get("fork"):
        score -= 2

    # Confidence is deliberately conservative: a wrong link is worse than a missing
    # one. HIGH (the only auto-applied tier) requires the coined method acronym to
    # appear in the repo *name*; short acronyms additionally need title overlap.
    long_acronym = len(mnorm) >= 4
    if acronym_in_name and (long_acronym or overlap >= 2):
        confidence = "HIGH"
    elif acronym_in_name or (acronym_in_text and overlap >= 2):
        confidence = "MEDIUM"
    elif overlap_ratio >= 0.5 and overlap >= 2:
        confidence = "LOW"
    else:
        confidence = "NONE"

    return {
        "full_name": full,
        "url": repo.get("html_url", ""),
        "description": desc[:160],
        "stars": repo.get("stargazers_count", 0),
        "fork": bool(repo.get("fork")),
        "score": round(score, 2),
        "overlap": overlap,
        "overlap_ratio": round(overlap_ratio, 2),
        "acronym_in_name": acronym_in_name,
        "confidence": confidence,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=0, help="cap papers processed (0 = all)")
    parser.add_argument("--delay", type=float, default=2.1, help="seconds between searches")
    args = parser.parse_args()

    gen = ReadmeGenerator(str(DATA))
    todo = [p for p in gen.papers if not gen.repo_link(p)]
    if args.limit:
        todo = todo[:args.limit]
    logger.info("Papers missing a code link: %d (processing %d)",
                sum(1 for p in gen.papers if not gen.repo_link(p)), len(todo))

    results: List[Dict[str, Any]] = []
    counts = {"VERIFIED": 0, "MEDIUM": 0, "LOW": 0, "NONE": 0}
    for i, paper in enumerate(todo, 1):
        title = gen.clean_text(paper["fields"].get("title", ""))
        method = clean_method(title)
        query = build_query(title, method)
        items = gh_search(query)
        scored = [score_candidate(title, method, r) for r in items]
        scored.sort(key=lambda c: c["score"], reverse=True)

        # Confirm via README: the top candidates that show any signal are checked for a
        # verbatim title match. The first that passes is an auto-applicable VERIFIED hit.
        verified = None
        for cand in [c for c in scored if c["overlap"] >= 1 or c["acronym_in_name"]][:3]:
            if title_in_readme(title, gh_readme(cand["full_name"])):
                cand["verified"] = True
                verified = cand
                break

        best = scored[0] if scored else None
        if verified:
            conf = "VERIFIED"
            chosen = verified
        elif best and best["confidence"] == "HIGH":
            conf, chosen = "MEDIUM", best          # acronym-in-name but README unconfirmed
        elif best and best["confidence"] in ("MEDIUM", "LOW"):
            conf, chosen = best["confidence"], best
        else:
            conf, chosen = "NONE", best
        counts[conf] = counts.get(conf, 0) + 1
        results.append({
            "citation_key": paper["citation_key"],
            "title": title,
            "method": method,
            "author": first_author_etal(paper),
            "query": query,
            "confidence": conf,
            "best": chosen,
            "alternatives": [c for c in scored[:3] if c is not chosen],
        })
        flag = {"VERIFIED": "✓", "MEDIUM": "?", "LOW": "·", "NONE": "✗"}[conf]
        logger.info("[%d/%d] %s %-8s %-38.38s -> %s", i, len(todo), flag, conf,
                    method or title, chosen["full_name"] if chosen else "—")
        if i < len(todo):
            time.sleep(args.delay)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump({"counts": counts, "candidates": results}, fh, indent=2, ensure_ascii=False)
    logger.info("\nDone. %s", counts)
    logger.info("Wrote %s", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
