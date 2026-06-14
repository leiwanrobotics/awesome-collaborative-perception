#!/usr/bin/env bash
# Regenerate the repository (tables + figures) from collaborative-perception.bib.
# Usage:  bash run_workflow.sh
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"

echo "[1/4] Parsing collaborative-perception.bib -> data/categorized_papers.json"
"$PY" tools/data_extraction/bib_parser.py

echo "[2/4] Rendering publication-statistics figure"
"$PY" tools/data_extraction/make_timeline_figure.py

echo "[3/4] Rendering per-table development timelines"
"$PY" tools/data_extraction/make_category_timelines.py

echo "[4/4] Generating README.md"
"$PY" tools/data_extraction/readme_generator.py

echo "Done. Review 'git diff' before committing."
