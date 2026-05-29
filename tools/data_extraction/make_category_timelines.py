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
XMIN, XMAX = 2018.6, 2026.7          # axis spans 2019 .. May 2026
PER_YEAR = 2                          # max representative works marked per year
SURVEY_C, SNOW_C = "#4C72B0", "#DD8452"


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


def select(gen, papers):
    by_year = defaultdict(list)
    for p in papers:
        y = year_of(p)
        if 2019 <= y <= 2026:
            by_year[y].append(p)
    chosen = []
    for y in sorted(by_year):
        ranked = sorted(by_year[y], key=lambda p: (-score(gen, p), short_label(p["fields"].get("title", "")).lower()))
        chosen.extend((y, p) for p in ranked[:PER_YEAR])
    return chosen


def render(title, chosen, gen, out: Path):
    # x within a year: spread multiple items across [-0.32, 0.32]
    by_year = defaultdict(list)
    for y, p in chosen:
        by_year[y].append(p)
    items = []  # (x, label, is_survey)
    for y in sorted(by_year):
        ps = by_year[y]
        offs = [0.0] if len(ps) == 1 else list(__import__("numpy").linspace(-0.3, 0.3, len(ps)))
        for off, p in zip(offs, ps):
            items.append((y + off, short_label(p["fields"]["title"]), not gen.is_snowball(p)))
    items.sort(key=lambda x: x[0])

    n = max(1, len(items))
    fig_w = max(8.0, min(20.0, 1.7 + n * 0.95))
    fig, ax = plt.subplots(figsize=(fig_w, 3.2))
    ax.axhline(0, color="#444444", lw=1.6, zorder=1)
    # year ticks
    for yr in range(2019, 2027):
        ax.plot([yr, yr], [-0.12, 0.12], color="#888888", lw=1, zorder=1)
        ax.text(yr, -0.42, "May 2026" if yr == 2026 else str(yr),
                ha="center", va="top", fontsize=9, color="#333333")

    levels = [1.0, -1.0, 1.7, -1.7]
    for i, (x, label, surv) in enumerate(items):
        lv = levels[i % len(levels)]
        c = SURVEY_C if surv else SNOW_C
        ax.plot([x, x], [0, lv], color=c, lw=0.9, alpha=0.7, zorder=1)
        ax.plot(x, 0, "o", color=c, ms=6, zorder=3)
        ax.text(x, lv + (0.12 if lv > 0 else -0.12), label, ha="center",
                va="bottom" if lv > 0 else "top", fontsize=8.5, color="#222222",
                rotation=0, zorder=4)

    ax.set_xlim(XMIN, XMAX)
    ax.set_ylim(-2.5, 2.5)
    ax.axis("off")
    ax.set_title(title, fontsize=12, fontweight="bold", pad=6)
    # legend
    ax.plot([], [], "o", color=SURVEY_C, label="Survey (SLR)")
    ax.plot([], [], "o", color=SNOW_C, label="Snowballing (2024–26)")
    ax.legend(loc="lower right", fontsize=8, frameon=False, ncol=2,
              bbox_to_anchor=(1.0, -0.02))
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=170, bbox_inches="tight")
    plt.close(fig)
    return len(items)


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
        chosen = select(g, papers)
        n = render(f"{title} — development timeline (2019 – May 2026)", chosen, g, OUTDIR / f"{key}.png")
        print(f"{key}: {len(papers)} papers, {n} representative works marked")


if __name__ == "__main__":
    main()
