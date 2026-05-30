#!/usr/bin/env python3
"""
README generator for Awesome Collaborative Perception.

The generated structure follows the survey paper:
"SLR on CP: A Computer Vision Perspective"
and renders each major classification as Markdown tables.
"""

import json
import re
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional


class ReadmeGenerator:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        with open(self.data_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        # All papers share the taxonomy tables. Papers tagged CP-Snowball come from
        # the forward-snowballing extension (2024–2026, beyond the survey's March-2024
        # cutoff); they are marked in a "Source" column so the surveyed 106 stay
        # identifiable, while the Publication Statistics still mirror the survey's
        # Table VIII (106 studies only).
        self.papers = self.data["papers"]
        self.snowball_papers = [p for p in self.papers if "CP-Snowball" in p.get("keywords", [])]
        self.survey_papers = [p for p in self.papers if "CP-Snowball" not in p.get("keywords", [])]

    def is_snowball(self, paper: Dict[str, Any]) -> bool:
        return "CP-Snowball" in paper.get("keywords", [])

    def source_label(self, paper: Dict[str, Any]) -> str:
        return "Snowball" if self.is_snowball(paper) else "Survey"

    def clean_text(self, value: str) -> str:
        if not value:
            return ""
        value = value.replace("\\n", " ").replace("\\t", " ")
        value = value.replace("{", "").replace("}", "")
        value = re.sub(r"\\\\texttimes", "x", value)
        value = re.sub(r"\\\\degree", "deg", value)
        value = re.sub(r"\\s+", " ", value).strip()
        return value

    def infer_modality(self, paper: Dict[str, Any]) -> str:
        keywords = set(paper.get("keywords", []))
        has_lidar = "CP-LiDAR" in keywords
        has_camera = "CP-Camera" in keywords
        if "CP-Fusion" in keywords or "CP-LiDAR-Camera" in keywords or (has_lidar and has_camera):
            return "LiDAR-Camera"
        if has_lidar:
            return "LiDAR"
        if has_camera:
            return "Camera"
        return "Agnostic"

    def infer_collaboration(self, paper: Dict[str, Any]) -> str:
        keywords = set(paper.get("keywords", []))
        if "CP-Early" in keywords:
            return "Early"
        if "CP-Intermediate" in keywords or "CP-Intermeidate" in keywords:
            return "Intermediate"
        if "CP-Late" in keywords:
            return "Late"
        if "CP-Hybrid" in keywords:
            return "Hybrid"
        # Datasets carry no fusion scheme; show their V2X configuration instead.
        has_v2v = "CP-V2V" in keywords
        has_v2i = "CP-V2I" in keywords
        if has_v2v and has_v2i:
            return "V2V & V2I"
        if has_v2v:
            return "V2V"
        if has_v2i:
            return "V2I"
        return "N/A"

    def infer_tasks(self, paper: Dict[str, Any]) -> List[str]:
        """Return ALL perception tasks a paper addresses.

        The survey assigns multiple tasks to several papers (e.g. V2VNet = OD + MP,
        BEV-V2X = SS + MP), so task membership must be multi-valued; using a single
        priority order previously collapsed task-agnostic / multi-task papers to zero.
        """
        keywords = set(paper.get("keywords", []))
        tasks: List[str] = []
        if "CP-Object Detection" in keywords:
            tasks.append("Object Detection")
        if "CP-Semantic Segmentation" in keywords:
            tasks.append("Semantic Segmentation")
        if "CP-Object Tracking" in keywords:
            tasks.append("Object Tracking")
        if "CP-Motion Prediction" in keywords or "CP-Prediction" in keywords:
            tasks.append("Motion Prediction")
        if "CP-Lane Detection" in keywords:
            tasks.append("Lane Detection")
        mt_kw = {"CP-Multi-task", "CP-Task-agnostic", "CP-Task Agnostic",
                 "CP-BEV Occupancy Prediction", "CP-Occupancy", "CP-BEV",
                 "CP-Scene Completion", "CP-Reconstruction"}
        if keywords & mt_kw:
            tasks.append("Multi-Task & Task-Agnostic")
        if "CP-Dataset" in keywords:
            tasks.append("Dataset / Benchmark")
        return tasks or ["Other"]

    def infer_task(self, paper: Dict[str, Any]) -> str:
        """Comma-joined task label for table display."""
        tasks = self.infer_tasks(paper)
        non_dataset = [t for t in tasks if t != "Dataset / Benchmark"]
        if non_dataset:
            return ", ".join(non_dataset)
        if "Dataset / Benchmark" in tasks:
            return "Dataset / Benchmark"
        return "Other"

    def paper_title(self, paper: Dict[str, Any]) -> str:
        return self.clean_text(paper["fields"].get("title", "Untitled"))

    def paper_venue(self, paper: Dict[str, Any]) -> str:
        fields = paper["fields"]
        venue = fields.get("booktitle") or fields.get("journal") or "N/A"
        return self.clean_text(venue)

    def paper_year(self, paper: Dict[str, Any]) -> str:
        return self.clean_text(str(paper["fields"].get("year", "N/A")))

    def paper_link(self, paper: Dict[str, Any]) -> str:
        fields = paper["fields"]
        doi = self.clean_text(fields.get("doi", ""))
        if doi:
            return f"https://doi.org/{doi}"
        eprint = self.clean_text(fields.get("eprint", ""))
        if eprint:
            return f"https://arxiv.org/abs/{eprint}"
        url = self.clean_text(fields.get("url", ""))
        if url:
            return url
        abstract = fields.get("abstract", "") or ""
        links = re.findall(r"https?://[^\s]+", abstract)
        for link in links:
            clean = link.rstrip(".,);]")
            if "github.com" not in clean and re.match(r"^https?://[^/]+\.[^/]+", clean):
                return clean
        return ""

    def repo_link(self, paper: Dict[str, Any]) -> str:
        code = self.clean_text(paper["fields"].get("code", ""))
        if code:
            return code.rstrip(".,);]")
        abstract = (paper["fields"].get("abstract") or "").replace(" ", "")
        match = re.search(r"https?://github\.com/[^\s,;\)\]]+", abstract)
        return match.group(0).rstrip(".,);]") if match else ""

    def format_link(self, url: str, label: str) -> str:
        return f"[{label}]({url})" if url else "—"

    def sort_papers(self, papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        def key(p: Dict[str, Any]):
            year = p["fields"].get("year", "0")
            try:
                year_num = int(re.sub(r"\D", "", str(year)) or "0")
            except ValueError:
                year_num = 0
            return (-year_num, self.paper_title(p).lower())

        return sorted(papers, key=key)

    def filter_by(self, *, modality: Optional[str] = None, collaboration: Optional[str] = None, task: Optional[str] = None, dataset_only: bool = False) -> List[Dict[str, Any]]:
        results = []
        for paper in self.papers:
            keywords = set(paper.get("keywords", []))
            if dataset_only and "CP-Dataset" not in keywords:
                continue
            if modality and self.infer_modality(paper) != modality:
                continue
            if collaboration and self.infer_collaboration(paper) != collaboration:
                continue
            if task and task not in self.infer_tasks(paper):
                continue
            results.append(paper)
        return self.sort_papers(results)

    def count(self, **kwargs: Any) -> int:
        return len(self.filter_by(**kwargs))

    def make_table(self, papers: List[Dict[str, Any]], columns: List[str]) -> str:
        header = "| " + " | ".join(columns) + " |\n"
        sep = "| " + " | ".join(["---"] * len(columns)) + " |\n"
        rows = []
        for paper in papers:
            data = {
                "Paper": self.paper_title(paper),
                "Venue": self.paper_venue(paper),
                "Year": self.paper_year(paper),
                "Modality": self.infer_modality(paper),
                "Collaboration": self.infer_collaboration(paper),
                "Task": self.infer_task(paper),
                "Paper Link": self.format_link(self.paper_link(paper), "Paper"),
                "Repo Link": self.format_link(self.repo_link(paper), "Repo"),
                "Source": self.source_label(paper),
            }
            rows.append("| " + " | ".join(data[c] for c in columns) + " |")
        return header + sep + "\n".join(rows) + "\n"

    def section(self, title: str, papers: List[Dict[str, Any]], columns: List[str],
                intro: str = "", timeline_key: str = "") -> str:
        body = f"### {title} ({len(papers)} papers)\n\n"
        if timeline_key:
            img = self.data_path.parent.parent / "figure" / "timeline" / f"{timeline_key}.png"
            if img.exists():
                body += (f'<p align="center">\n'
                         f'<img src="figure/timeline/{timeline_key}.png" width="95%" height="auto" '
                         f'alt="{title} development timeline"/>\n</p>\n\n')
        if intro:
            body += intro + "\n\n"
        if papers:
            body += self.make_table(papers, columns) + "\n"
        else:
            body += "_No papers classified under this section yet._\n\n"
        return body

    def generate_header(self) -> str:
        total = len(self.papers)
        n_survey = len(self.survey_papers)
        n_snow = len(self.snowball_papers)
        today = date.today().isoformat()
        repo = "leiwanrobotics/awesome-collaborative-perception"
        pdf = "A_Systematic_Literature_Review_on_Vehicular_Collaborative_PerceptionA_Computer_Vision_Perspective.pdf"
        updated_badge = today.replace("-", "--")
        return f"""# Awesome Collaborative Perception [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, continuously maintained index of **vehicular collaborative perception** research, organized by the taxonomy of our survey *"A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective"* (IEEE T-ITS, 2026).

<div align="center">

[![Survey](https://img.shields.io/badge/Survey-PDF-b31b1b.svg)]({pdf})
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Papers](https://img.shields.io/badge/papers-{total}-1f6feb.svg)
![Updated](https://img.shields.io/badge/updated-{updated_badge}-2ea44f.svg)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![Stars](https://img.shields.io/github/stars/{repo}?style=social)](https://github.com/{repo}/stargazers)

</div>

<p align="center">
<img src="figure/CP.png" width="55%" height="auto"/>
</p>

**Vehicular collaborative perception** — also called cooperative or collective perception — lets connected vehicles and roadside infrastructure exchange sensor information over V2V / V2I / V2X links to see through occlusions and beyond line of sight, overcoming the fundamental limits of single-vehicle perception. This repository is a continuously maintained index of **{total} peer-reviewed papers (2019–2026)**, each classified along three axes — **modality**, **collaboration scheme**, and **perception task** — with direct links to the paper and to official code when available.

The collection is built in two reproducible stages:

- **Systematic review** — {n_survey} studies (≤ March 2024) selected with a PRISMA-style protocol (Tables I–XXIX of the survey).
- **Forward-snowballing extension** — {n_snow} studies (2024–2026) discovered from the citation graph of the surveyed papers and screened with the same inclusion / exclusion criteria.

Every row is tagged **`Survey`** or **`Snowball`** in the *Source* column. The [Publication Statistics](#publication-statistics) mirror the survey's Table VIII (the {n_survey} surveyed studies); the per-section tables additionally include the snowballing extension. All artifacts are regenerated from [`collaborative-perception.bib`](collaborative-perception.bib) by the scripts in [`tools/`](tools/README.md) — contributions welcome (see [Contributing](#contributing)).

## Table of Contents

- [Related Reviews](#related-reviews)
- [Publication Statistics](#publication-statistics)
- [Structured Taxonomy](#structured-taxonomy)
- [Modality Type](#modality-type)
  - [LiDAR](#lidar)
  - [Camera](#camera)
  - [LiDAR-Camera](#lidar-camera)
- [Collaboration Type](#collaboration-type)
  - [Early Collaboration](#early-collaboration)
  - [Intermediate Collaboration](#intermediate-collaboration)
  - [Late Collaboration](#late-collaboration)
  - [Hybrid Collaboration](#hybrid-collaboration)
- [Perception Tasks](#perception-tasks)
  - [Collaborative Object Detection](#collaborative-object-detection)
  - [Collaborative Semantic Segmentation](#collaborative-semantic-segmentation)
  - [Collaborative Object Tracking](#collaborative-object-tracking)
  - [Collaborative Motion Prediction](#collaborative-motion-prediction)
  - [Collaborative Lane Detection](#collaborative-lane-detection)
  - [Multi-Task and Task-Agnostic](#multi-task-and-task-agnostic)
- [Datasets](#datasets)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

## Related Reviews

| Review | Year | Publication | Focus |
| --- | ---: | --- | --- |
| Bai et al. | 2022 | IEEE T-ITS | High-level overview of CP architecture and node structure |
| Caillot et al. | 2022 | IEEE T-ITS | Focus on localization, object detection, and tracking |
| Han et al. | 2023 | IEEE ITS Magazine | CP methods for both ideal and adverse scenarios |
| Liu et al. | 2023 | arXiv | Introduction to CP issues |
| Huang et al. | 2024 | arXiv | Framework proposal for CP |

Relative to these, our survey adds a transparent PRISMA-style selection protocol, a unified modality / collaboration / task taxonomy, and a computer-vision-centric comparative analysis — which this repository operationalizes as a living, reproducible index.

---

"""

    def generate_statistics(self) -> str:
        """Publication statistics reproducing the survey's Table VIII verbatim.

        Table VIII reports aggregate, unique-study counts. These are the survey's
        official headline figures and are mirrored here exactly so the repository
        stays consistent with the paper. The per-section tables below enumerate the
        same 106 studies following the per-method Tables IX–XXIX; small per-axis
        differences from Table VIII stem from the survey's unique-study aggregation
        and an "Agnostic" modality bucket that Table VIII does not break out.
        """
        lines = [
            "## Publication Statistics\n",
            "These figures mirror **Table VIII** of the survey (aggregate, unique-study counts) so the repository stays consistent with the paper.\n",
            "| Dimension | Categories (survey Table VIII) |",
            "| --- | --- |",
            "| **Modality** | LiDAR (63), Camera (13), LiDAR-Camera (12) |",
            "| **Collaboration** | Early (6), Intermediate (71), Late (15), Hybrid (6) |",
            "| **Task** | Object Detection (78), Semantic Segmentation (6), Object Tracking (5), Motion Prediction (3), Lane Detection (2), Multi-task (3), Task-agnostic (8) |",
            "| **Region** | Asia (54), North America (38), Europe (13), Africa (1) |",
            "| **Top venues** | ICRA (16), CVPR (8), IEEE T-IV (8), NeurIPS (8), ICCV (5), IEEE RA-L (5), IEEE ITSC (5), IEEE T-ITS (4), IEEE IoTJ (4), IEEE IV (4) |",
            "",
            "> These counts cover the **106 surveyed studies only**. The taxonomy tables below additionally include the forward-snowballing extension (2024–2026), with each row marked `Survey` or `Snowball` in the **Source** column. Per-section counts therefore exceed these figures; minor differences between the surveyed sections and Table VIII arise from the survey's unique-study aggregation and an *Agnostic* modality bucket not separated in Table VIII.",
            "",
            "Publications over time across all 402 collected papers (survey vs forward-snowballing, by modality, collaboration, and task):",
            "",
            '<p align="center">',
            '<img src="figure/development_timeline.png" width="92%" height="auto" alt="Publication statistics over time"/>',
            "</p>",
            "",
            "<sub>Regenerate with <code>python tools/data_extraction/make_timeline_figure.py</code>. Survey collection ≤ March 2024; 2024–2026 extended via forward snowballing; 2026 is partial.</sub>",
            "\n---\n",
        ]
        return "\n".join(lines)

    def generate_taxonomy(self) -> str:
        return """## Structured Taxonomy

Papers are organized along the three axes of the survey, so the repository works as a practical lookup index rather than a flat list:

1. **Modality** — *LiDAR*, *Camera*, *LiDAR-Camera*, and *Modality-Agnostic* (e.g. object-level late fusion).
2. **Collaboration scheme** — *Early* (raw-data sharing), *Intermediate* (feature sharing), *Late* (result sharing), and *Hybrid*.
3. **Perception task** — *Object Detection*, *Semantic Segmentation*, *Object Tracking*, *Motion Prediction*, *Lane Detection*, and *Multi-Task / Task-Agnostic*.

The same study appears under each axis it belongs to, and a per-table **development timeline** precedes every table to trace how that category evolved.

**Table key.** &nbsp; **Year** — publication year. &nbsp; **Modality / Collaboration / Task** — taxonomy labels above (datasets show their V2X mode, *V2V* / *V2I*, in the Collaboration column). &nbsp; **Paper** / **Repo** — links to the publication and official code. &nbsp; **Source** — `Survey` (in the SLR, ≤ Mar 2024) or `Snowball` (forward-snowballing extension, 2024–2026).

---

"""

    def generate_modality_sections(self) -> str:
        columns = ["Paper", "Venue", "Year", "Collaboration", "Task", "Paper Link", "Repo Link", "Source"]
        body = "## Modality Type\n\n"
        body += self.section("LiDAR", self.filter_by(modality="LiDAR"), columns, timeline_key="mod_lidar")
        body += self.section("Camera", self.filter_by(modality="Camera"), columns, timeline_key="mod_camera")
        body += self.section("LiDAR-Camera", self.filter_by(modality="LiDAR-Camera"), columns, timeline_key="mod_lidar-camera")
        body += self.section("Modality-Agnostic / Other", self.filter_by(modality="Agnostic"), columns, timeline_key="mod_agnostic")
        body += "---\n\n"
        return body

    def generate_collaboration_sections(self) -> str:
        columns = ["Paper", "Venue", "Year", "Modality", "Task", "Paper Link", "Repo Link", "Source"]
        body = "## Collaboration Type\n\n"
        body += self.section("Early Collaboration", self.filter_by(collaboration="Early"), columns, timeline_key="collab_early")
        body += self.section("Intermediate Collaboration", self.filter_by(collaboration="Intermediate"), columns, timeline_key="collab_intermediate")
        body += self.section("Late Collaboration", self.filter_by(collaboration="Late"), columns, timeline_key="collab_late")
        body += self.section("Hybrid Collaboration", self.filter_by(collaboration="Hybrid"), columns, timeline_key="collab_hybrid")
        body += "---\n\n"
        return body

    def generate_task_sections(self) -> str:
        columns = ["Paper", "Venue", "Year", "Modality", "Collaboration", "Paper Link", "Repo Link", "Source"]
        body = "## Perception Tasks\n\n"
        body += self.section("Collaborative Object Detection", self.filter_by(task="Object Detection"), columns, timeline_key="task_object-detection")
        body += self.section("Collaborative Semantic Segmentation", self.filter_by(task="Semantic Segmentation"), columns, timeline_key="task_semantic-segmentation")
        body += self.section("Collaborative Object Tracking", self.filter_by(task="Object Tracking"), columns, timeline_key="task_object-tracking")
        body += self.section("Collaborative Motion Prediction", self.filter_by(task="Motion Prediction"), columns, timeline_key="task_motion-prediction")
        body += self.section("Collaborative Lane Detection", self.filter_by(task="Lane Detection"), columns, timeline_key="task_lane-detection")
        body += self.section("Multi-Task and Task-Agnostic", self.filter_by(task="Multi-Task & Task-Agnostic"), columns, timeline_key="task_multi-task")
        body += "---\n\n"
        return body

    def generate_dataset_section(self) -> str:
        columns = ["Paper", "Venue", "Year", "Modality", "Collaboration", "Paper Link", "Repo Link", "Source"]
        body = "## Datasets\n\n"
        body += self.section("Dataset / Benchmark Papers", self.filter_by(dataset_only=True), columns, timeline_key="dataset")
        body += "---\n\n"
        return body

    def generate_footer(self) -> str:
        return r"""## Contributing

Contributions are welcome — to add a missing paper, correct a classification, or fix a link:

1. Add a BibTeX entry to [`collaborative-perception.bib`](collaborative-perception.bib) with the
   taxonomy keywords described in [`tools/README.md`](tools/README.md) — e.g.
   `keywords = {CP-LiDAR, CP-Intermediate, CP-Object Detection}`. Tag papers found beyond the
   survey's March-2024 cutoff with `CP-Snowball`, and add `code = {https://github.com/...}` when
   official code exists.
2. Regenerate the tables and figures, then open a pull request:

```bash
pip install -r requirements.txt
bash run_workflow.sh   # parses the .bib, rebuilds the figures and README.md
```

Do not edit `README.md` by hand — it is generated. The source of truth is the `.bib` file.
See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Citation

If this index or the underlying survey is useful in your research, please cite:

```bibtex
@article{wan2026slr,
  title   = {A Systematic Literature Review on Vehicular Collaborative Perception:
             A Computer Vision Perspective},
  author  = {Wan, Lei and Zhao, Jianxin and Wiedholz, Andreas and Bied, Manuel and
             Martinez de Lucena, Mateus and Jagtap, Abhishek Dinkar and Festag, Andreas and
             Fr{\"o}hlich, Ant{\^o}nio Augusto and Keen, Hannan Ejaz and Vinel, Alexey},
  journal = {IEEE Transactions on Intelligent Transportation Systems},
  year    = {2026},
  doi     = {10.1109/TITS.2025.3631141}
}
```

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
"""

    def generate_full_readme(self, output_path: str):
        readme = ""
        readme += self.generate_header()
        readme += self.generate_statistics()
        readme += self.generate_taxonomy()
        readme += self.generate_modality_sections()
        readme += self.generate_collaboration_sections()
        readme += self.generate_task_sections()
        readme += self.generate_dataset_section()
        readme += self.generate_footer()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(readme)

        print(f"README generated at: {output_path}")


def main():
    data_path = Path(__file__).parent.parent.parent / "data" / "categorized_papers.json"
    output_path = Path(__file__).parent.parent.parent / "README.md"

    print("Generating README from categorized papers...")
    generator = ReadmeGenerator(str(data_path))
    generator.generate_full_readme(str(output_path))
    print("README.md generated successfully!")


if __name__ == "__main__":
    main()
