# Contributing

Thanks for helping keep this index accurate and current. Contributions can be as small as a fixed
link or as large as a batch of new papers.

## The golden rule

`README.md` and everything under `figure/` are **generated**. The single source of truth is
[`collaborative-perception.bib`](collaborative-perception.bib). Edit the `.bib` file, regenerate, and
commit both — never hand-edit `README.md`.

## Add or fix a paper

1. Add (or correct) a BibTeX entry in `collaborative-perception.bib`. Include:
   - `title`, `author`, `year`, and a venue (`booktitle` for conferences, `journal` for journals);
   - `doi` or `eprint` (arXiv id) so the **Paper** link resolves;
   - `code = {https://github.com/...}` if official open-source code exists (the **Repo** link);
   - `keywords` following the convention in [`tools/README.md`](tools/README.md), e.g.
     `keywords = {CP-LiDAR, CP-Intermediate, CP-Object Detection}`.
   - Tag any paper published after the survey's March-2024 cutoff with `CP-Snowball`.

2. Regenerate and open a pull request:

   ```bash
   pip install -r requirements.txt
   bash run_workflow.sh        # parses the bib, rebuilds figures and README.md
   ```

3. In the PR, note the paper's venue/year and why it is in scope (vehicular multi-agent
   collaborative perception with a perception task). Please verify links resolve.

## Scope

In scope: vehicular collaborative / cooperative perception over V2V, V2I, or V2X, with a perception
task (detection, segmentation, tracking, motion prediction, lane detection, occupancy, multi-task),
or a dataset/benchmark for it. Out of scope: single-vehicle perception, pure communication/networking
without a perception model, and non-vehicular multi-agent settings.

## Style

- Keep BibTeX keys descriptive and unique.
- Prefer the published venue over the preprint when both exist.
- One logical change per pull request; conventional-commit messages are appreciated.
