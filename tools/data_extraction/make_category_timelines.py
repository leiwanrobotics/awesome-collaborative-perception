#!/usr/bin/env python3
"""Render a horizontal development timeline for each taxonomy table.

For every category table in the README (modality, collaboration, task, datasets) this
draws a 2019 → May-2026 timeline with that category's representative works marked on it.
To keep the timelines legible and high-signal, only works published at **top venues**
(CVPR, ICCV, ECCV, TPAMI, IJCV, NeurIPS, ICLR, ICML, AAAI, IJCAI, ICRA, IROS, RA-L, CoRL,
T-RO, T-ITS, T-IV, T-IP, ACM MM) are marked.

Each work is labelled "<VENUE><YEAR> <approach>" (e.g. "CVPR2026 V2VNet"). The approach
name is the method's own name when the paper gives one (an acronym, a CamelCase token, a
short pre-colon name, or a parenthesised acronym); when the paper names no method, the
label falls back to "<First-author surname> et al." instead.

Outputs: figure/timeline/<key>.png
"""
import re
import sys
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
MAXLAB = 34                           # label truncation length (venue+year+approach)
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


# Broader venue acronyms, used only on the fallback path (a category with < 3 top-venue
# works) so that every marked label can still carry a venue prefix.
EXTRA_VENUES = [
    (r"intelligent transportation systems conference|\bITSC\b", "ITSC"),
    (r"intelligent vehicles symposium|\bIV\b", "IV"),
    (r"connected and automated vehicles|\bCAVS\b", "CAVS"),
    (r"robotics and autonomous systems", "RAS"),
    (r"internet of things journal", "IoTJ"),
    (r"ieee access", "Access"),
    (r"\bsensors\b", "Sensors"),
    (r"\bremote sensing\b", "RemoteSens"),
    (r"transactions on vehicular technology", "T-VT"),
    (r"transactions on mobile computing", "TMC"),
    (r"arxiv|corr", "arXiv"),
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


def venue_short(paper):
    """A short venue acronym for *any* venue (top-venue acronym, then broader matches,
    then a parenthesised acronym in the venue string, else a trimmed venue name)."""
    acro = venue_acronym(paper)
    if acro:
        return acro
    v = paper["fields"].get("booktitle") or paper["fields"].get("journal") or ""
    v = re.sub(r"[{}]", " ", v)
    v = re.sub(r"\s+", " ", v).strip()
    for pat, a in EXTRA_VENUES:
        if re.search(pat, v, re.I):
            return a
    m = re.search(r"\(([A-Za-z][A-Za-z0-9\-]{1,7})\)", v)
    if m:
        return m.group(1)
    v = re.sub(r"^\d+\s*(st|nd|rd|th)?\s*", "", v)            # drop a leading edition number
    v = re.sub(r"^(IEEE|ACM)\s+", "", v, flags=re.I).strip()
    return (v[:10] or "misc")


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
    "3d", "2d", "4d",
}


def _atom_is_acronym(s: str) -> bool:
    """Whether a single hyphen-free atom reads as a coined name rather than a plain word.

    True for all-caps acronyms (DUSA, CORE), CamelCase / internal-caps tokens (CoBEVT,
    ViT, HPLaw), and letter+digit codes (V2X). False for ordinary Capitalised words
    (Multi, Latency, Keypoints) so descriptive phrases fall back to "<author> et al.".
    """
    if not s or not s.isalnum():
        return False
    n_alpha = sum(c.isalpha() for c in s)
    if s.isupper() and n_alpha >= 2:                     # DUSA, CORE, DI
        return True
    if any(c.isupper() for c in s[1:]):                  # CoBEVT, ViT, HPLaw
        return True
    if any(c.isdigit() for c in s) and n_alpha >= 1 and len(s) >= 3:  # V2X, S2R
        return True
    return False


def _looks_like_name(w: str) -> bool:
    """Whether a (possibly hyphenated) title token is a coined method name."""
    if len(w) > 16 or not w.replace("-", "").isalnum():
        return False
    parts = w.split("-")
    if len(parts) > 1:                                   # V2X-ViT yes, Multi-Agent no
        return any(_atom_is_acronym(p) for p in parts)
    return _atom_is_acronym(w)


def method_name(title: str):
    """Return the method's own name if the title states one, else None.

    A name is taken from (in order): a short pre-colon name (e.g. "V2VNet: ..."), a
    parenthesised acronym (e.g. "... (V2I-MSF) ..."), or the first distinctive
    acronym / CamelCase token, skipping generic adjectives. Returns None when the title
    describes the approach only in plain words — the caller then falls back to "X et al.".
    """
    t = re.sub(r"\s+", " ", title.replace("{", "").replace("}", "")).strip()
    if ":" in t:
        pre = t.split(":")[0].strip(" .,")
        if 1 <= len(pre) <= 24 and len(pre.split()) <= 3 and pre.lower() not in _GENERIC:
            return pre
    # parenthesised acronym, e.g. "(V2I-MSF)", "(CoBEVT)"
    m = re.search(r"\(([A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])\)", t)
    if m and _looks_like_name(m.group(1)):
        return m.group(1)
    toks = [w.strip(".,") for w in t.split()]
    # prefer a coined acronym / CamelCase token (e.g. CoBEVT, V2X-ViT, BEV-V2X)
    for w in toks[:6]:
        if w.lower() not in _GENERIC and _looks_like_name(w):
            return w
    return None


def first_author_etal(paper) -> str:
    """"<surname> et al." (or just "<surname>" for a sole author) from the author field.

    Handles both "Last, First and …" and "First Last and …" BibTeX author formats.
    """
    raw = paper["fields"].get("author", "") or ""
    authors = [a.strip() for a in re.split(r"\s+and\s+", raw) if a.strip()]
    if not authors:
        return "et al."
    first = re.sub(r"[{}\\\"]", "", authors[0]).strip()
    surname = first.split(",")[0].strip() if "," in first else first.split()[-1]
    return f"{surname} et al." if len(authors) > 1 else surname


def display_name(paper) -> str:
    """The method name if the paper gives one, else "<first-author surname> et al."."""
    return method_name(paper["fields"].get("title", "")) or first_author_etal(paper)


def score(gen, p) -> int:
    s = 2 if not gen.is_snowball(p) else 0          # survey landmarks first
    if method_name(p["fields"].get("title", "")):
        s += 1                                       # named method ranked above "X et al."
    return s


def truncate(s):
    return s if len(s) <= MAXLAB else s[:MAXLAB - 1].rstrip() + "…"


def select(gen, papers):
    """Per-year lists of (label, is_survey) for TOP-VENUE works only.

    Label = "<VENUE><YEAR> <approach>" (e.g. "CVPR2026 V2VNet"); survey landmarks are
    ranked first, then capped with a "+N more" overflow marker per year. When a category
    has fewer than three top-venue works, all works are shown with a broader venue acronym.
    """
    top = [p for p in papers if venue_acronym(p)]
    fallback = len(top) < 3   # too few flagship works: show all, broad-venue prefix
    by_year = {y: [] for y in YEARS}
    pool = papers if fallback else top
    for p in pool:
        y = year_of(p)
        if y in by_year:
            by_year[y].append(p)
    cols = {}
    for y in YEARS:
        ranked = sorted(by_year[y], key=lambda p: (-score(gen, p), display_name(p).lower()))
        rows = []
        for p in ranked[:CAP]:
            label = truncate(f"{venue_short(p)}{y} {display_name(p)}")
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
