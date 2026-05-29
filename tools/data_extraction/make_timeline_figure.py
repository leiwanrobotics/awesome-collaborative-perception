#!/usr/bin/env python3
"""Render the Development Timeline as a publication-style multi-panel figure.

Reads data/categorized_papers.json (402 papers = 106 surveyed + 296 forward-snowballing)
and draws per-year stacked bars for the field's development trajectory along four views:
total (survey vs snowball), modality, collaboration scheme, and perception task.

Output: figure/development_timeline.png
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "tools" / "data_extraction"))
from readme_generator import ReadmeGenerator  # noqa: E402

YEARS = list(range(2019, 2027))


def year_of(gen, p):
    import re
    try:
        return int(re.sub(r"\D", "", str(p["fields"].get("year", "0"))) or 0)
    except ValueError:
        return 0


def stack(ax, cats, data, colors, title, ylabel="Publications"):
    bottom = [0] * len(YEARS)
    for cat in cats:
        vals = [data[cat].get(y, 0) for y in YEARS]
        ax.bar(YEARS, vals, bottom=bottom, label=cat, color=colors[cat],
               edgecolor="white", linewidth=0.5, width=0.8)
        bottom = [b + v for b, v in zip(bottom, vals)]
    ax.set_title(title, fontsize=12, fontweight="bold", pad=8)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.set_xticks(YEARS)
    ax.set_xticklabels([f"'{str(y)[2:]}" for y in YEARS], fontsize=9)
    ax.tick_params(axis="y", labelsize=9)
    ax.grid(axis="y", alpha=0.25, linewidth=0.6)
    ax.set_axisbelow(True)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.legend(fontsize=8, frameon=False, ncol=1, loc="upper left")


def main():
    g = ReadmeGenerator(str(ROOT / "data/categorized_papers.json"))

    src = defaultdict(lambda: defaultdict(int))
    mod = defaultdict(lambda: defaultdict(int))
    col = defaultdict(lambda: defaultdict(int))
    tsk = defaultdict(lambda: defaultdict(int))
    for p in g.papers:
        y = year_of(g, p)
        if y not in YEARS:
            continue
        src["Snowball (2024–26)" if g.is_snowball(p) else "Survey (SLR)"][y] += 1
        mod[g.infer_modality(p)][y] += 1
        c = g.infer_collaboration(p)
        if c in ("Early", "Intermediate", "Late", "Hybrid"):
            col[c][y] += 1
        for t in g.infer_tasks(p):
            if t not in ("Other", "Dataset / Benchmark"):
                tsk[t][y] += 1

    C = plt.get_cmap("tab10").colors
    src_c = {"Survey (SLR)": "#4C72B0", "Snowball (2024–26)": "#DD8452"}
    mod_c = {"LiDAR": C[0], "Camera": C[1], "LiDAR-Camera": C[2], "Agnostic": "#B0B0B0"}
    col_c = {"Early": C[2], "Intermediate": C[0], "Late": C[3], "Hybrid": C[4]}
    tsk_order = ["Object Detection", "Semantic Segmentation", "Object Tracking",
                 "Motion Prediction", "Lane Detection", "Multi-Task & Task-Agnostic"]
    tsk_c = {t: C[i] for i, t in enumerate(tsk_order)}

    fig, axes = plt.subplots(2, 2, figsize=(12, 8.2))
    fig.suptitle("Development Timeline of Vehicular Collaborative Perception (2019–2026)",
                 fontsize=14, fontweight="bold", y=0.98)

    stack(axes[0, 0], ["Survey (SLR)", "Snowball (2024–26)"], src, src_c,
          "Publications per year (by source)")
    stack(axes[0, 1], ["LiDAR", "Camera", "LiDAR-Camera", "Agnostic"], mod, mod_c,
          "By modality")
    stack(axes[1, 0], ["Early", "Intermediate", "Late", "Hybrid"], col, col_c,
          "By collaboration scheme")
    stack(axes[1, 1], tsk_order, tsk, tsk_c, "By perception task (multi-label)")

    fig.text(0.5, 0.005,
             "Survey collection ≤ March 2024 (106 studies); 2024–2026 extended via forward "
             "snowballing (296 studies). 2026 is partial.",
             ha="center", fontsize=8, style="italic", color="#555555")
    fig.tight_layout(rect=[0, 0.02, 1, 0.96])

    out = ROOT / "figure" / "development_timeline.png"
    fig.savefig(out, dpi=200, bbox_inches="tight")
    print("wrote", out)


if __name__ == "__main__":
    main()
