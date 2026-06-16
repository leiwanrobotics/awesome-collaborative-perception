# Changelog

All notable changes to this repository are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- **"Approaches to Address Realistic Issues" section** (survey Section VII): a
  fourth, cross-cutting taxonomy view grouping methods by the real-world deployment
  problem they relax — localization / pose error, time latency, communication
  efficiency, communication robustness, domain shift, heterogeneity, and adversarial
  robustness — each as a collapsible table with its own development timeline.
- Realistic-issue classification of all 402 papers (survey ground-truth from
  Tables XIV–XVIII + ROBOSAC/V2X-INCOP, plus abstract-level reading of the 296
  forward-snowballing papers via their Zotero full text). 259 papers carry ≥1 issue
  tag: pose 44, latency 49, comm-efficiency 140, comm-robustness 28, domain 27,
  heterogeneity 41, adversarial 11.
- New keyword axis (`CP-Pose-Error`, `CP-Latency`, `CP-Comm-Efficiency`,
  `CP-Comm-Robust`, `CP-Domain-Gap`, `CP-Heterogeneous`, `CP-Adversarial`) and two
  helper scripts (`extract_zotero_abstracts.py`, `apply_issue_keywords.py`).

## [1.0.0] — 2026-05-31

First public release: a reproducible, taxonomy-organized index of vehicular
collaborative perception research accompanying the IEEE T-ITS 2026 survey.

### Added
- **402 curated papers (2019–2026)** classified along three axes — modality,
  collaboration scheme, and perception task — each linked to its publication and
  official code when available.
- **Forward-snowballing extension**: 296 studies (2024–2026) discovered from the
  citation graph of the surveyed papers and screened against the survey's
  inclusion/exclusion criteria, tagged `Snowball` in the *Source* column.
- **Per-table development timelines** marking top-venue works as
  `VENUE+YEAR approach` (e.g. `CVPR2024 RCooper`).
- Reproducible tooling in `tools/` that regenerates the README and all figures from
  the single source of truth `collaborative-perception.bib` (`bash run_workflow.sh`).
- Committed snowballing provenance (screening verdicts + finalized keep set) under
  `data/snowballing/` for auditability.
- `CITATION.cff`, machine-readable citation metadata.

### Changed
- Survey badge now links to the stable IEEE T-ITS DOI rather than a bundled PDF.

[1.0.0]: https://github.com/leiwanrobotics/awesome-collaborative-perception/releases/tag/v1.0.0
