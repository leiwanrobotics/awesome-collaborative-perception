# Maintenance Tooling

This directory contains the scripts that turn [`collaborative-perception.bib`](../collaborative-perception.bib)
(the single source of truth) into the repository's `README.md` and figures, and that extend the
collection via reproducible forward snowballing.

> `README.md` is **generated** — never edit it by hand. Edit the `.bib` file, then re-run the
> generators below (or `bash ../run_workflow.sh`).

## Layout

```
tools/
├── data_extraction/
│   ├── bib_parser.py              # .bib  -> data/categorized_papers.json (uses bibtexparser)
│   ├── readme_generator.py        # categorized_papers.json -> README.md
│   ├── make_timeline_figure.py    # -> figure/development_timeline.png (publication statistics)
│   └── make_category_timelines.py # -> figure/timeline/*.png (per-table timelines)
├── snowballing/
│   ├── forward_snowballing.py     # citing papers via Semantic Scholar / OpenCitations
│   ├── consolidate.py             # merge + dedup screened candidates
│   ├── enrich_links.py            # recover DOIs via Semantic Scholar title search
│   ├── crossref_enrich.py         # recover remaining DOIs via Crossref
│   └── append_snowball.py         # write accepted papers into the .bib (tagged CP-Snowball)
├── study_selection/
│   └── llm_classifier.py          # optional LLM screening (legacy, SiliconFlow); see note below
└── add_paper.py                   # interactive single-paper helper
```

Install dependencies once: `pip install -r ../requirements.txt`.

## Keyword convention

Each BibTeX entry is classified by `keywords`. The generator reads these to place a paper in the
right tables.

| Axis | Keywords |
| --- | --- |
| Modality | `CP-LiDAR`, `CP-Camera` (use both for LiDAR-Camera); none ⇒ *Agnostic* |
| Collaboration | `CP-Early`, `CP-Intermediate`, `CP-Late`, `CP-Hybrid` |
| Task | `CP-Object Detection`, `CP-Semantic Segmentation`, `CP-Object Tracking`, `CP-Motion Prediction`, `CP-Lane Detection`, `CP-Task-agnostic` |
| Dataset | `CP-Dataset` (+ `CP-V2V` / `CP-V2I` for its V2X mode) |
| Source | `CP-Snowball` for papers beyond the survey's March-2024 cutoff |

A paper may carry several task keywords (e.g. `CP-Object Detection, CP-Motion Prediction`); it then
appears in each corresponding table. The optional `code = {https://github.com/...}` field renders the
**Repo** link.

Example:

```bibtex
@inproceedings{example2024,
  title    = {Example: A Cooperative Detector},
  author   = {Doe, Jane and Smith, John},
  booktitle = {Proc. IEEE/CVF CVPR},
  year     = {2024},
  doi      = {10.1109/CVPR.2024.00000},
  code     = {https://github.com/example/repo},
  keywords = {CP-LiDAR, CP-Intermediate, CP-Object Detection},
}
```

## Regenerate the repository

```bash
bash ../run_workflow.sh
# equivalently:
python data_extraction/bib_parser.py
python data_extraction/make_timeline_figure.py
python data_extraction/make_category_timelines.py
python data_extraction/readme_generator.py
```

## Extend via forward snowballing

The collection beyond March 2024 is built by snowballing the citation graph of the surveyed papers
and screening candidates against the survey's inclusion/exclusion criteria (IC1–IC4, EC1–EC6).

```bash
# 1. discover citing papers (Semantic Scholar + OpenCitations, public APIs, rate-limited)
python snowballing/forward_snowballing.py            # -> data/snowballing/new_candidates.json

# 2. screen candidates against IC/EC (see repo history for the two-pass screening that
#    produced the accepted set)

# 3. consolidate + recover identifiers
python snowballing/consolidate.py
python snowballing/enrich_links.py
python snowballing/crossref_enrich.py                # Crossref is the reliable title->DOI source

# 4. append accepted papers to the .bib (tagged CP-Snowball) and regenerate
python snowballing/append_snowball.py
bash ../run_workflow.sh
```

### Note on `study_selection/llm_classifier.py`

This is an **optional, legacy** helper that applies IC/EC via the SiliconFlow API and requires
`SILICONFLOW_API_KEY`. The screening used to build the current extension was performed against the
same criteria without it, so this script is provided only as a convenience for fully automated runs
and is not required to reproduce the repository.

## API notes

- **Semantic Scholar** graph API — no key required, but the keyless tier is heavily rate-limited;
  expect partial results on large runs (use the Crossref fallback for DOIs).
- **OpenCitations** / **Crossref** — lenient; Crossref prefers a `mailto` in the User-Agent.
- **Papers with Code** — its public API is discontinued (returns HTML), so repo links are taken only
  from author-stated GitHub URLs in abstracts.
