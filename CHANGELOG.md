# Changelog

All notable changes to this repository are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
