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

        all_papers = self.data["papers"]
        # Papers tagged CP-Snowball come from the forward-snowballing extension
        # (2024–2026, beyond the survey's March-2024 cutoff). They are kept in a
        # separate section so the surveyed 106 stay faithful to the paper.
        self.snowball_papers = [p for p in all_papers if "CP-Snowball" in p.get("keywords", [])]
        self.papers = [p for p in all_papers if "CP-Snowball" not in p.get("keywords", [])]

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
            }
            rows.append("| " + " | ".join(data[c] for c in columns) + " |")
        return header + sep + "\n".join(rows) + "\n"

    def section(self, title: str, papers: List[Dict[str, Any]], columns: List[str], intro: str = "") -> str:
        body = f"### {title} ({len(papers)} papers)\n\n"
        if intro:
            body += intro + "\n\n"
        if papers:
            body += self.make_table(papers, columns) + "\n"
        else:
            body += "_No papers classified under this section yet._\n\n"
        return body

    def generate_header(self) -> str:
        total = len(self.papers)
        today = date.today().isoformat()
        return f"""# Awesome Collaborative Perception [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
<a href="A_Systematic_Literature_Review_on_Vehicular_Collaborative_PerceptionA_Computer_Vision_Perspective.pdf"><img src="https://img.shields.io/badge/Paper-PDF-red.svg" alt="Paper Badge"/></a>
<a href="https://github.com/lei-wan/awesome-collaborative-perception/stargazers"><img src="https://img.shields.io/github/stars/lei-wan/awesome-collaborative-perception" alt="Stars Badge"/></a>
<a href="https://github.com/lei-wan/awesome-collaborative-perception/network/members"><img src="https://img.shields.io/github/forks/lei-wan/awesome-collaborative-perception" alt="Forks Badge"/></a>
<a href="https://github.com/lei-wan/awesome-collaborative-perception/issues"><img src="https://img.shields.io/github/issues/lei-wan/awesome-collaborative-perception" alt="Issues Badge"/></a>
</div>

This repository is organized directly around our survey paper, **"A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective"** (*IEEE T-ITS, 2026*). Instead of a loose awesome-list, the README follows the survey taxonomy and presents each major classification as a structured Markdown table with paper metadata, paper links, and repository links when available.

- Survey scope: vehicular collaborative perception from a computer vision perspective
- Current collection: **{total} papers**
- Source of truth: `collaborative-perception.bib`
- Generated from: `tools/data_extraction/readme_generator.py`
- Last generated: `{today}`

<p align="center">
<img src="figure/CP.png" width="50%" height="auto"/>
</p>

## Table of Contents

- [Related Reviews](#related-reviews)
- [Publication Statistics](#publication-statistics)
- [Structured Taxonomy](#structured-taxonomy)
- [Development Timeline](#development-timeline)
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
- [Forward-Snowballing Extension (2024–2026)](#forward-snowballing-extension-20242026)
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

Our survey emphasizes a PRISMA-style SLR process, a structured taxonomy, and a computer-vision-centric analysis of collaborative perception.

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
            "> The per-section tables below enumerate the same studies from the survey's per-method Tables IX–XXIX. Minor per-axis count differences versus Table VIII arise from the survey's unique-study aggregation and an *Agnostic* modality not separated in Table VIII.",
            "\n---\n",
        ]
        return "\n".join(lines)

    def generate_taxonomy(self) -> str:
        return """## Structured Taxonomy

The README follows the same three major axes used in the survey:

1. **Modality Type**: LiDAR, Camera, and LiDAR-Camera.
2. **Collaboration Type**: Early, Intermediate, Late, and Hybrid collaboration.
3. **Perception Tasks**: Object Detection, Semantic Segmentation, Object Tracking, Motion Prediction, Lane Detection, and Multi-Task / Task-Agnostic settings.

Every section below is rendered as a table so the repository can be used as a practical lookup index rather than only a narrative overview.

---

"""

    def generate_timeline(self) -> str:
        """Per-axis development-trajectory diagrams (Mermaid timelines).

        Milestone methods are drawn from the survey's per-method Tables IX–XXIX;
        per-year counts are computed from the 106-paper collection.
        """
        return """## Development Timeline

Development trajectory of vehicular collaborative perception along the three taxonomy axes
(milestone methods from the survey's Tables IX–XXIX; per-year counts from this collection).

### Modality trajectory

LiDAR anchored the field from the start; camera-only CP emerged around 2021–2023 and
LiDAR–camera fusion from 2022, but LiDAR still dominates (63 vs 13 vs 12 in the survey).

```mermaid
timeline
    title Modality evolution in Collaborative Perception
    2019 : LiDAR debut — F-cooper
    2020 : LiDAR scales — V2VNet, When2com / Who2com
    2021 : LiDAR matures : first camera CP — Distilled Co-Graph
    2022 : LiDAR–camera fusion arrives — V2X-ViT, HGAN, Where2comm : datasets OPV2V, V2X-Sim
    2023 : Peak LiDAR (29) : camera CP grows — CoCa3D, HM-ViT : fusion V2VFusion
    2024 : LiDAR sustained (19) : fusion HEAL, EMIFF, ActFormer, ViT-FuseNet
```

### Collaboration trajectory

Intermediate (feature-level) fusion became and stayed dominant (71); early, late and hybrid
schemes remain comparatively rare.

```mermaid
timeline
    title Collaboration-type evolution
    2019 : Intermediate begins — F-cooper, F-Transformer
    2020 : Intermediate grows — V2VNet : first late fusion
    2021 : Late fusion — FL-Dynamic
    2022 : Early collaboration — JointPerception : first hybrid — Pillar-based CP
    2023 : Intermediate peaks (30) : late fusion grows — Among Us, Collective PV-RCNN
    2024 : Intermediate sustained (20) : hybrid — FreeAlign, Hybrid-CP, ML-Cooper
```

### Perception-task trajectory

Object detection dominated from the outset (78); segmentation, tracking, motion prediction,
lane detection and multi-task / task-agnostic settings emerged and broadened later.

```mermaid
timeline
    title Perception-task evolution
    2019 : Object detection — F-cooper
    2020 : Detection scales : lane detection — Co-mapping
    2021 : Semantic segmentation — Who2com / When2com (CSS)
    2022 : Detection dominant : task-agnostic scene completion — STAR
    2023 : Tracking — HYDRO-3D : motion prediction : task-agnostic — Core
    2024 : Multi-modal occupancy — CoHFF : cooperative tracking — Probabilistic 3D-MOT
```

---

"""

    def generate_modality_sections(self) -> str:
        columns = ["Paper", "Venue", "Year", "Collaboration", "Task", "Paper Link", "Repo Link"]
        body = "## Modality Type\n\n"
        body += self.section("LiDAR", self.filter_by(modality="LiDAR"), columns)
        body += self.section("Camera", self.filter_by(modality="Camera"), columns)
        body += self.section("LiDAR-Camera", self.filter_by(modality="LiDAR-Camera"), columns)
        body += "---\n\n"
        return body

    def generate_collaboration_sections(self) -> str:
        columns = ["Paper", "Venue", "Year", "Modality", "Task", "Paper Link", "Repo Link"]
        body = "## Collaboration Type\n\n"
        body += self.section("Early Collaboration", self.filter_by(collaboration="Early"), columns)
        body += self.section("Intermediate Collaboration", self.filter_by(collaboration="Intermediate"), columns)
        body += self.section("Late Collaboration", self.filter_by(collaboration="Late"), columns)
        body += self.section("Hybrid Collaboration", self.filter_by(collaboration="Hybrid"), columns)
        body += "---\n\n"
        return body

    def generate_task_sections(self) -> str:
        columns = ["Paper", "Venue", "Year", "Modality", "Collaboration", "Paper Link", "Repo Link"]
        body = "## Perception Tasks\n\n"
        body += self.section("Collaborative Object Detection", self.filter_by(task="Object Detection"), columns)
        body += self.section("Collaborative Semantic Segmentation", self.filter_by(task="Semantic Segmentation"), columns)
        body += self.section("Collaborative Object Tracking", self.filter_by(task="Object Tracking"), columns)
        body += self.section("Collaborative Motion Prediction", self.filter_by(task="Motion Prediction"), columns)
        body += self.section("Collaborative Lane Detection", self.filter_by(task="Lane Detection"), columns)
        body += self.section("Multi-Task and Task-Agnostic", self.filter_by(task="Multi-Task & Task-Agnostic"), columns)
        body += "---\n\n"
        return body

    def generate_dataset_section(self) -> str:
        columns = ["Paper", "Venue", "Year", "Modality", "Task", "Paper Link", "Repo Link"]
        body = "## Datasets\n\n"
        body += self.section("Dataset / Benchmark Papers", self.filter_by(dataset_only=True), columns)
        body += "---\n\n"
        return body

    def snowball_table(self, papers: List[Dict[str, Any]]) -> str:
        columns = ["Paper", "Venue", "Year", "Modality", "Collaboration", "Task", "Paper Link"]
        header = "| " + " | ".join(columns) + " |\n"
        sep = "| " + " | ".join(["---"] * len(columns)) + " |\n"
        rows = []
        for paper in self.sort_papers(papers):
            data = {
                "Paper": self.paper_title(paper),
                "Venue": self.paper_venue(paper),
                "Year": self.paper_year(paper),
                "Modality": self.infer_modality(paper),
                "Collaboration": self.infer_collaboration(paper),
                "Task": self.infer_task(paper),
                "Paper Link": self.format_link(self.paper_link(paper), "Paper"),
            }
            rows.append("| " + " | ".join(data[c] for c in columns) + " |")
        return header + sep + "\n".join(rows) + "\n"

    def generate_snowball_section(self) -> str:
        if not self.snowball_papers:
            return ""
        n = len(self.snowball_papers)
        body = "## Forward-Snowballing Extension (2024–2026)\n\n"
        body += (
            f"The survey's literature collection was finalized in **March 2024**. Following the survey's own "
            f"recommendation to *\"apply forward snowballing to update the review with cutting-edge research beyond "
            f"the collection period,\"* the **{n} papers** below were discovered by forward snowballing (Semantic "
            f"Scholar / OpenCitations citation graph of the 106 surveyed papers) and screened with the same "
            f"inclusion/exclusion criteria (IC1–IC4, EC1–EC6). They are listed separately and are **not** counted in "
            f"the survey statistics above.\n\n"
        )
        tasks = [
            ("Object Detection", "Object Detection"),
            ("Semantic Segmentation", "Semantic Segmentation"),
            ("Object Tracking", "Object Tracking"),
            ("Motion Prediction", "Motion Prediction"),
            ("Lane Detection", "Lane Detection"),
            ("Multi-Task & Task-Agnostic", "Multi-Task and Task-Agnostic"),
            ("Dataset / Benchmark", "Datasets and Benchmarks"),
        ]
        for key, title in tasks:
            papers = [p for p in self.snowball_papers if key in self.infer_tasks(p)]
            if papers:
                body += f"### {title} ({len(papers)} papers)\n\n"
                body += self.snowball_table(papers) + "\n"
        body += "---\n\n"
        return body

    def generate_footer(self) -> str:
        return """## Citation

If you find this repository useful, please cite our survey paper:

```bibtex
@article{wan2026systematic,
  title={A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective},
  author={Wan, Lei and others},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2026}
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
        readme += self.generate_timeline()
        readme += self.generate_modality_sections()
        readme += self.generate_collaboration_sections()
        readme += self.generate_task_sections()
        readme += self.generate_dataset_section()
        readme += self.generate_snowball_section()
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
