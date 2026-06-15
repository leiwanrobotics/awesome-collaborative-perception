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
│   ├── append_snowball.py         # write accepted papers into the .bib (tagged CP-Snowball)
│   ├── find_code_repos.py         # discover missing code repos via GitHub search (README-verified)
│   └── apply_code_repos.py        # write VERIFIED code repos into the .bib
├── study_selection/
│   └── llm_classifier.py          # optional LLM screening (legacy, SiliconFlow); see note below
└── add_paper.py                   # interactive single-paper helper
```

`data/categorized_papers.json` is a **generated** artifact (the parsed `.bib`, shared by the
README and figure scripts); refresh it via `bash ../run_workflow.sh`, never edit it by hand.

Install dependencies once: `pip install -r ../requirements.txt` (Python ≥ 3.9).

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

The collection beyond March 2024 is grown by snowballing the citation graph of the surveyed
papers and screening the citing works against the survey's inclusion/exclusion criteria
(IC1–IC4, EC1–EC6). The current extension added **296 studies (2024–2026)**.

> **Run every command from the repository root.** `forward_snowballing.py` (its `--output-dir`
> default) and `crossref_enrich.py` resolve paths relative to the current directory, so running
> from `tools/` would read/write the wrong locations.

The pipeline is a chain of JSON files under `data/snowballing/`. Two steps are human-in-the-loop
(marked ⚙︎): screening the candidates, and finalizing the keep set.

```text
data/categorized_papers.json                         seed = the surveyed papers
  │  forward_snowballing.py        Semantic Scholar + OpenCitations + arXiv (rate-limited)
  ▼
forward_snowballing_<ts>.json  +  new_candidates.json     deduped citing papers
  │  ⚙︎ screen against IC1–IC4 / EC1–EC6   (two-pass; working data in batches/, pass2/)
  ▼
data/snowballing/screened/accepted_*.json
  │  consolidate.py                merge + dedup vs the .bib; flag borderline papers
  ▼
data/snowballing/accepted_consolidated.json
  │  ⚙︎ finalize the keep set
  ▼
data/snowballing/kept_final.json
  │  enrich_links.py               recover doi/arxiv/url via Semantic Scholar title search
  ▼
data/snowballing/kept_enriched.json
  │  crossref_enrich.py            recover remaining DOIs via Crossref (updates in place)
  ▼
data/snowballing/kept_enriched.json
  │  append_snowball.py            write CP-Snowball entries into the .bib
  ▼
collaborative-perception.bib  →  bash run_workflow.sh  →  README.md + figures
```

```bash
# 1. discover citing papers (public APIs, rate-limited; writes a timestamped file and
#    new_candidates.json under data/snowballing/)
python tools/snowballing/forward_snowballing.py

# 2. ⚙︎ screen candidates against IC1–IC4 / EC1–EC6  ->  data/snowballing/screened/accepted_*.json
#    (optional automated screener: tools/study_selection/llm_classifier.py; see note below)

# 3. consolidate the screened set (dedups against the existing .bib, flags borderline papers)
python tools/snowballing/consolidate.py              # -> accepted_consolidated.json

# 4. ⚙︎ finalize the kept papers as data/snowballing/kept_final.json

# 5. recover links / identifiers for the kept papers
python tools/snowballing/enrich_links.py             # kept_final.json -> kept_enriched.json
CROSSREF_MAILTO="you@example.com" \
python tools/snowballing/crossref_enrich.py          # Crossref is the reliable title->DOI source

# 6. append the kept papers to the .bib (tagged CP-Snowball) and regenerate the repo
python tools/snowballing/append_snowball.py
bash run_workflow.sh
```

The human-decision artifacts of this pipeline — `data/snowballing/screened/accepted_*.json`
(screening verdicts) and `data/snowballing/kept_final.json` (finalized keep set) — are committed
so the 2024–2026 extension is auditable; the bulky raw candidate dumps stay gitignored.

### Recover missing code repositories

Papers With Code is discontinued, so official repositories are recovered via GitHub search and
confirmed by checking that the candidate repo's README quotes the paper title verbatim — a
high-precision signal that avoids linking coincidental keyword matches.

```bash
# 1. search GitHub for each paper lacking a code link; writes a reviewable candidates file
#    (VERIFIED = README-confirmed; LOW/NONE are not applied). Throttled to GitHub's 30 req/min.
python tools/snowballing/find_code_repos.py        # -> data/snowballing/code_candidates.json

# 2. write the VERIFIED matches into the .bib (skips entries that already have a code field),
#    then regenerate. Add reviewed lower-confidence keys with --also-keys k1,k2
python tools/snowballing/apply_code_repos.py
bash run_workflow.sh
```

Requires an authenticated `gh` CLI (`gh auth status`). `code_candidates.json` is committed as an
audit trail of what was found and verified.

### Note on `study_selection/llm_classifier.py`

This is an **optional, legacy** helper that applies IC/EC via the SiliconFlow API and requires
`SILICONFLOW_API_KEY`. The screening used to build the current extension was performed against the
same criteria without it, so this script is provided only as a convenience for fully automated runs
and is not required to reproduce the repository. The criteria themselves are recorded, in
human-readable form, in [`config/inclusion_criteria.json`](../config/inclusion_criteria.json)
(a reference document, not loaded by any script).

## API notes

- **Semantic Scholar** graph API — no key required, but the keyless tier is heavily rate-limited;
  expect partial results on large runs (use the Crossref fallback for DOIs).
- **OpenCitations** / **Crossref** — lenient; Crossref prefers a `mailto` in the User-Agent. Set
  yours via the `CROSSREF_MAILTO` environment variable (a neutral default is used otherwise).
- **Papers with Code** — its public API is discontinued (now redirects to Hugging Face), so code
  links come from author-stated GitHub URLs in abstracts plus README-verified GitHub search
  (`find_code_repos.py`).
- **GitHub** — `find_code_repos.py` uses the authenticated `gh` CLI (search API, ~30 req/min).
