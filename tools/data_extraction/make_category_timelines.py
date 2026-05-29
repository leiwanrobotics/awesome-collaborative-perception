#!/usr/bin/env python3
"""Render a horizontal development timeline for each taxonomy table.

For every category table in the README (modality, collaboration, task, datasets) this
draws a 2019 → May-2026 timeline with that category's representative works marked on it.
Representative works are selected from the collection (survey landmarks first, then
named-acronym snowballing papers), capped per year for readability.

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
CAP = 18                              # max works listed per year before "+N more"
MAXLAB = 26                           # label truncation length
SURVEY_C, SNOW_C = "#1f5fa6", "#d2691e"


def year_of(p):
    try:
        return int(re.sub(r"\D", "", str(p["fields"].get("year", "0"))) or 0)
    except ValueError:
        return 0


def short_label(title: str) -> str:
    t = re.sub(r"\s+", " ", title.replace("{", "").replace("}", "")).strip()
    if ":" in t:
        pre = t.split(":")[0].strip()
        if 1 <= len(pre) <= 22:
            return pre
    toks = t.split()
    if toks and re.search(r"[A-Z0-9]", toks[0]) and len(toks[0]) <= 16:
        return toks[0].strip(".,")
    return " ".join(toks[:2])


def score(gen, p) -> int:
    s = 2 if not gen.is_snowball(p) else 0          # survey landmarks first
    if ":" in (p["fields"].get("title", "")):
        s += 1                                       # named-acronym method
    return s


def truncate(s):
    return s if len(s) <= MAXLAB else s[:MAXLAB - 1].rstrip() + "…"


def select(gen, papers):
    """Per-year lists of (label, is_survey), survey landmarks first; cap with overflow."""
    by_year = {y: [] for y in YEARS}
    for p in papers:
        y = year_of(p)
        if y in by_year:
            by_year[y].append(p)
    cols = {}
    for y in YEARS:
        ranked = sorted(by_year[y], key=lambda p: (-score(gen, p),
                                                    short_label(p["fields"].get("title", "")).lower()))
        rows = [(truncate(short_label(p["fields"]["title"])), not gen.is_snowball(p)) for p in ranked[:CAP]]
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
        n = render(f"{title} — development timeline (2019 – May 2026)", cols, OUTDIR / f"{key}.png")
        print(f"{key}: {len(papers)} papers, {n} works shown")


if __name__ == "__main__":
    main()
