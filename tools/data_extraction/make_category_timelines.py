#!/usr/bin/env python3
"""Render a horizontal development timeline for each taxonomy table.

For every category table in the README (modality, collaboration, task, datasets) this
draws a 2019 → May-2026 timeline with that category's representative works marked on it.
To keep the timelines legible and high-signal, only works published at **top venues**
(CVPR, ICCV, ECCV, TPAMI, IJCV, NeurIPS, ICLR, ICML, AAAI, IJCAI, ICRA, IROS, RA-L, CoRL,
T-RO, T-ITS, T-IV, T-IP, ACM MM) are marked; each label is prefixed with its venue.

Outputs: figure/timeline/<key>.png
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "data_extraction"))
from readme_generator import ReadmeGenerator  # noqa: E402

OUTDIR = ROOT / "figure" / "timeline"
YEARS = list(range(2019, 2027))       # 2019 .. May 2026
CAP = 12                              # max works listed per year before "+N more"
MAXLAB = 30                           # label truncation length
SURVEY_C, SNOW_C = "#1f5fa6", "#d2691e"

# Top venues only (flagship CV / ML / robotics / ITS). Ordered: first match wins.
# Workshops are excluded explicitly in venue_acronym().
TOP_VENUES = [
    (r"pattern analysis and machine intelligence", "TPAMI"),
    (r"international journal of computer vision", "IJCV"),
    (r"computer vision and pattern recognition|\bCVPR\b", "CVPR"),
    (r"international conference on computer vision|\bICCV\b", "ICCV"),
    (r"european conference on computer vision|\bECCV\b", "ECCV"),
    (r"neural information processing|neurips|\bnips\b|adv\. neural", "NeurIPS"),
    (r"learning representations|\bICLR\b", "ICLR"),
    (r"international conference on machine learning|\bICML\b", "ICML"),
    (r"\baaai\b", "AAAI"),
    (r"ijcai|international joint conference on artificial", "IJCAI"),
    (r"robot learning|\bCoRL\b", "CoRL"),
    (r"transactions on robotics", "T-RO"),
    (r"robotics and automation letters", "RA-L"),
    (r"robotics and automation|\bICRA\b", "ICRA"),
    (r"intelligent robots and systems|\bIROS\b", "IROS"),
    (r"transactions on intelligent transportation", "T-ITS"),
    (r"transactions on intelligent vehicles", "T-IV"),
    (r"transactions on image processing", "T-IP"),
    (r"acm.*multimedia|\bACM MM\b", "ACM MM"),
]


def venue_acronym(paper):
    """Return the flagship-venue acronym for a paper, or None if not a top venue."""
    v = paper["fields"].get("booktitle") or paper["fields"].get("journal") or ""
    v = re.sub(r"[{}]", " ", v)
    v = re.sub(r"\s+", " ", v).strip()
    if "workshop" in v.lower():
        return None
    for pat, acro in TOP_VENUES:
        if re.search(pat, v, re.I):
            return acro
    return None


def year_of(p):
    try:
        return int(re.sub(r"\D", "", str(p["fields"].get("year", "0"))) or 0)
    except ValueError:
        return 0


_GENERIC = {
    "a", "an", "the", "towards", "toward", "learning", "enhancing", "enhanced",
    "robust", "efficient", "cooperative", "collaborative", "improving", "improved",
    "rethinking", "boosting", "exploring", "bridging", "is", "on", "multi", "multi-modal",
    "deep", "real-time", "real", "from", "what", "when", "how", "vehicle-to-infrastructure",
    "vehicle-to-vehicle", "vehicle-road", "scalable", "generative", "practical", "advanced",
    "unified", "context-aware", "adaptive", "distance-aware", "uncertainty",
}


def short_label(title: str) -> str:
    """Pick a compact, distinctive method name from a paper title.

    Prefers an explicit method name before a colon (e.g. "V2VNet: ..."); otherwise the
    first distinctive token (acronym/CamelCase) skipping generic adjectives.
    """
    t = re.sub(r"\s+", " ", title.replace("{", "").replace("}", "")).strip()
    if ":" in t:
        pre = t.split(":")[0].strip()
        if 1 <= len(pre) <= 24:
            return pre
    toks = [w.strip(".,") for w in t.split()]
    # prefer an acronym / CamelCase token (e.g. CoBEVT, V2X-ViT, BEV-V2X)
    for w in toks[:6]:
        core = w.replace("-", "")
        if len(w) <= 16 and core.isalnum() and (
            sum(c.isupper() for c in w) >= 2 or any(ch.isdigit() for ch in w)
        ) and w.lower() not in _GENERIC:
            return w
    # else first non-generic token
    for w in toks:
        if w.lower() not in _GENERIC and len(w) >= 3:
            return w if len(w) <= 16 else w[:15] + "…"
    return " ".join(toks[:2])


def score(gen, p) -> int:
    s = 2 if not gen.is_snowball(p) else 0          # survey landmarks first
    if ":" in (p["fields"].get("title", "")):
        s += 1                                       # named-acronym method
    return s


def truncate(s):
    return s if len(s) <= MAXLAB else s[:MAXLAB - 1].rstrip() + "…"


def select(gen, papers):
    """Per-year lists of (label, is_survey) for TOP-VENUE works only.

    Label = "<VENUE> <ShortName>"; survey landmarks are ranked first, then capped with
    a "+N more" overflow marker per year.
    """
    top = [(p, venue_acronym(p)) for p in papers if venue_acronym(p)]
    fallback = len(top) < 3   # too few flagship works: show all, no venue prefix
    by_year = {y: [] for y in YEARS}
    pool = papers if fallback else [p for p, _ in top]
    for p in pool:
        y = year_of(p)
        if y in by_year:
            by_year[y].append((p, None if fallback else venue_acronym(p)))
    cols = {}
    for y in YEARS:
        ranked = sorted(by_year[y], key=lambda pa: (-score(gen, pa[0]),
                                                    short_label(pa[0]["fields"].get("title", "")).lower()))
        rows = []
        for p, acro in ranked[:CAP]:
            name = short_label(p["fields"]["title"])
            label = truncate(f"{acro} {name}" if acro else name)
            rows.append((label, not gen.is_snowball(p)))
        extra = len(ranked) - CAP
        if extra > 0:
            rows[-1] = (f"+{extra + 1} more", None)
        cols[y] = (rows, len(by_year[y]))
    return cols


def render(title, cols, out: Path):
    maxrows = max((len(r) for r, _ in cols.values()), default=1)
    fig_w = 15.5
    fig_h = max(2.4, 1.15 + maxrows * 0.235)
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))

    x = {y: i for i, y in enumerate(YEARS)}
    top = maxrows + 0.3
    ax.axhline(0, color="#444444", lw=1.4, zorder=2)
    for y in YEARS:
        xi = x[y]
        ax.axvline(xi, ymin=0.06, ymax=0.97, color="#e6e6e6", lw=0.8, zorder=0)
        ax.plot([xi, xi], [-0.18, 0.18], color="#888888", lw=1.2, zorder=2)
        ax.text(xi, -0.55, "May 2026" if y == 2026 else str(y),
                ha="center", va="top", fontsize=10, fontweight="bold", color="#333333")
        rows, total = cols[y]
        for r, (label, surv) in enumerate(rows):
            c = "#999999" if surv is None else (SURVEY_C if surv else SNOW_C)
            ax.text(xi, 0.55 + r * 1.0, label, ha="center", va="bottom",
                    fontsize=7.4, color=c,
                    style="italic" if surv is None else "normal", zorder=3)

    ax.set_xlim(-0.6, len(YEARS) - 0.4)
    ax.set_ylim(-1.2, top + 0.6)
    ax.axis("off")
    ax.set_title(title, fontsize=13, fontweight="bold", pad=8)
    ax.plot([], [], "s", color=SURVEY_C, label="Survey (SLR, ≤ Mar 2024)")
    ax.plot([], [], "s", color=SNOW_C, label="Snowballing (2024–26)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.0), fontsize=8.5,
              frameon=False, ncol=2)
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return sum(len(r) for r, _ in cols.values())


def main():
    g = ReadmeGenerator(str(ROOT / "data/categorized_papers.json"))
    specs = [
        ("LiDAR collaborative perception", {"modality": "LiDAR"}, "mod_lidar"),
        ("Camera collaborative perception", {"modality": "Camera"}, "mod_camera"),
        ("LiDAR-Camera collaborative perception", {"modality": "LiDAR-Camera"}, "mod_lidar-camera"),
        ("Modality-agnostic / other", {"modality": "Agnostic"}, "mod_agnostic"),
        ("Early collaboration", {"collaboration": "Early"}, "collab_early"),
        ("Intermediate collaboration", {"collaboration": "Intermediate"}, "collab_intermediate"),
        ("Late collaboration", {"collaboration": "Late"}, "collab_late"),
        ("Hybrid collaboration", {"collaboration": "Hybrid"}, "collab_hybrid"),
        ("Collaborative object detection", {"task": "Object Detection"}, "task_object-detection"),
        ("Collaborative semantic segmentation", {"task": "Semantic Segmentation"}, "task_semantic-segmentation"),
        ("Collaborative object tracking", {"task": "Object Tracking"}, "task_object-tracking"),
        ("Collaborative motion prediction", {"task": "Motion Prediction"}, "task_motion-prediction"),
        ("Collaborative lane detection", {"task": "Lane Detection"}, "task_lane-detection"),
        ("Multi-task & task-agnostic", {"task": "Multi-Task & Task-Agnostic"}, "task_multi-task"),
        ("Datasets & benchmarks", {"dataset_only": True}, "dataset"),
    ]
    for title, flt, key in specs:
        papers = g.filter_by(**flt)
        cols = select(g, papers)
        n = render(f"{title} — development timeline (2019 – May 2026, top-venue works)",
                   cols, OUTDIR / f"{key}.png")
        print(f"{key}: {len(papers)} papers, {n} top-venue works shown")


if __name__ == "__main__":
    main()
