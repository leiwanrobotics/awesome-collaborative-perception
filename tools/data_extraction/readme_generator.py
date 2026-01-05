#!/usr/bin/env python3
"""
README Generator for Awesome Collaborative Perception Repository
Generates a comprehensive README based on the categorized papers.
"""

import json
from pathlib import Path
from typing import Dict, List, Any
from bib_parser import BibTeXParser


class ReadmeGenerator:
    """Generates README.md from categorized papers."""

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        with open(self.data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        self.papers_dict = {p['citation_key']: p for p in self.data['papers']}

    def generate_header(self) -> str:
        """Generate README header."""
        header = """# Awesome Collaborative Perception [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of papers and resources on **Vehicular Collaborative Perception** from a Computer Vision perspective.

This repository accompanies our systematic literature review paper:

**"A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective"**
*IEEE Transactions on Intelligent Transportation Systems (T-ITS), 2026*

📄 [Paper PDF](A_Systematic_Literature_Review_on_Vehicular_Collaborative_PerceptionA_Computer_Vision_Perspective.pdf) | 🔗 [BibTeX](collaborative-perception.bib)

## About Collaborative Perception

Collaborative perception (CP) enables multiple vehicles and infrastructure to share sensory information, creating a comprehensive understanding of the traffic environment. This approach overcomes the limitations of single-vehicle perception such as occlusions, limited sensing range, and sparse observations.

### Key Features
- 🚗 **V2V & V2I Communication**: Vehicle-to-Vehicle and Vehicle-to-Infrastructure
- 📊 **109 Papers**: Comprehensive collection from systematic literature review (2019-2024)
- 🏷️ **Organized Taxonomy**: By modality, collaboration type, and perception task
- 📈 **PRISMA 2020**: Follows systematic review guidelines

---

## Table of Contents

- [Statistics](#statistics)
- [Taxonomy](#taxonomy)
  - [By Modality](#by-modality)
  - [By Collaboration Type](#by-collaboration-type)
  - [By Perception Task](#by-perception-task)
- [Papers](#papers)
  - [LiDAR-based Methods](#lidar-based-methods)
  - [Camera-based Methods](#camera-based-methods)
  - [Early Collaboration](#early-collaboration)
  - [Intermediate Collaboration](#intermediate-collaboration)
  - [Late Collaboration](#late-collaboration)
  - [Hybrid Collaboration](#hybrid-collaboration)
  - [Object Detection](#object-detection)
  - [Object Tracking](#object-tracking)
  - [Semantic Segmentation](#semantic-segmentation)
  - [Motion Prediction & Lane Detection](#motion-prediction--lane-detection)
- [Tools](#tools)
- [Contributing](#contributing)
- [Citation](#citation)
- [License](#license)

---

## Statistics

"""
        stats = self.data['statistics']
        header += f"**Total Papers**: {stats['total_papers']}\n\n"

        header += "| Category | Count |\n"
        header += "|----------|-------|\n"

        header += "| **Modality** | |\n"
        for modality, count in stats['by_modality'].items():
            header += f"| └─ {modality} | {count} |\n"

        header += "| **Collaboration Type** | |\n"
        for collab, count in stats['by_collaboration'].items():
            header += f"| └─ {collab} | {count} |\n"

        header += "| **Perception Task** | |\n"
        for task, count in stats['by_task'].items():
            header += f"| └─ {task} | {count} |\n"

        header += "\n---\n\n"
        return header

    def generate_taxonomy_section(self) -> str:
        """Generate taxonomy overview section."""
        section = """## Taxonomy

Our systematic literature review categorizes collaborative perception methods along three dimensions:

### By Modality

- **LiDAR-based**: Methods using 3D point cloud data from LiDAR sensors
- **Camera-based**: Methods using 2D RGB images from cameras
- **LiDAR-Camera Fusion**: Methods combining both modalities

### By Collaboration Type

- **Early Collaboration**: Sharing raw sensor data (point clouds, images)
- **Intermediate Collaboration**: Sharing intermediate feature representations
- **Late Collaboration**: Sharing detection/prediction results
- **Hybrid Collaboration**: Combining multiple collaboration strategies

### By Perception Task

- **Object Detection**: 3D bounding box detection
- **Object Tracking**: Multi-object tracking across time
- **Semantic Segmentation**: Point-wise or pixel-wise classification
- **Motion Prediction**: Future trajectory forecasting
- **Lane Detection**: Road structure understanding
- **Multi-task**: Multiple perception tasks simultaneously

---

## Papers

"""
        return section

    def format_paper_entry(self, citation_key: str) -> str:
        """Format a single paper entry."""
        paper = self.papers_dict.get(citation_key)
        if not paper:
            return ""

        fields = paper['fields']

        # Extract and clean title
        title = fields.get('title', 'Untitled')
        title = title.replace('{', '').replace('}', '')

        # Extract authors
        author = fields.get('author', 'Unknown')
        authors = author.split(' and ')
        if len(authors) > 3:
            author_str = f"{authors[0]} et al."
        else:
            author_str = ', '.join(authors)

        # Extract year
        year = fields.get('year', 'N/A')

        # Extract venue
        venue = fields.get('booktitle') or fields.get('journal', 'N/A')
        venue = venue.replace('{', '').replace('}', '')

        # Extract DOI
        doi = fields.get('doi', '')

        # Format entry
        entry = f"- **{title}**  \n"
        entry += f"  {author_str}  \n"
        entry += f"  *{venue}*, {year}"

        if doi:
            entry += f"  \n  [[DOI](https://doi.org/{doi})]"

        # Add arXiv if available
        arxiv = fields.get('eprint', '')
        if arxiv:
            entry += f" [[arXiv](https://arxiv.org/abs/{arxiv})]"

        entry += "\n"

        return entry

    def generate_category_section(self, category_name: str, papers: List[str]) -> str:
        """Generate a section for a specific category."""
        section = f"### {category_name}\n\n"
        section += f"**{len(papers)} papers**\n\n"

        for citation_key in sorted(papers):
            section += self.format_paper_entry(citation_key)

        section += "\n"
        return section

    def generate_papers_sections(self) -> str:
        """Generate all paper listing sections."""
        sections = ""

        # By Modality
        categories = self.data['categories']

        sections += self.generate_category_section(
            "LiDAR-based Methods",
            categories['modality'].get('LiDAR', [])
        )

        sections += self.generate_category_section(
            "Camera-based Methods",
            categories['modality'].get('Camera', [])
        )

        # By Collaboration Type
        sections += self.generate_category_section(
            "Early Collaboration",
            categories['collaboration'].get('Early', [])
        )

        sections += self.generate_category_section(
            "Intermediate Collaboration",
            categories['collaboration'].get('Intermediate', [])
        )

        sections += self.generate_category_section(
            "Late Collaboration",
            categories['collaboration'].get('Late', [])
        )

        sections += self.generate_category_section(
            "Hybrid Collaboration",
            categories['collaboration'].get('Hybrid', [])
        )

        # By Task
        sections += self.generate_category_section(
            "Object Detection",
            categories['task'].get('Object Detection', [])
        )

        sections += self.generate_category_section(
            "Object Tracking",
            categories['task'].get('Object Tracking', [])
        )

        sections += self.generate_category_section(
            "Semantic Segmentation",
            categories['task'].get('Semantic Segmentation', [])
        )

        # Combine Motion Prediction and Lane Detection
        motion_papers = categories['task'].get('Motion Prediction', [])
        lane_papers = categories['task'].get('Lane Detection', [])
        combined = list(set(motion_papers + lane_papers))

        sections += self.generate_category_section(
            "Motion Prediction & Lane Detection",
            combined
        )

        return sections

    def generate_tools_section(self) -> str:
        """Generate tools section."""
        section = """---

## Tools

This repository includes automated tools for systematic literature review:

### 📚 BibTeX Parser
Parse and categorize papers from BibTeX files based on keywords.

```bash
python tools/data_extraction/bib_parser.py
```

### 🔄 Forward Snowballing Tool
Automatically discover new papers that cite existing works.

```bash
python tools/snowballing/forward_snowballing.py
```

### 🤖 LLM-based Study Selection
Automated study selection using LLM to apply inclusion/exclusion criteria.

```bash
python tools/study_selection/llm_classifier.py
```

See [tools/README.md](tools/README.md) for detailed documentation.

---

"""
        return section

    def generate_footer(self) -> str:
        """Generate README footer."""
        footer = """## Contributing

We welcome contributions! If you know of papers that should be included, please:

1. Check if the paper meets our [inclusion criteria](docs/inclusion_criteria.md)
2. Add the BibTeX entry to `collaborative-perception.bib` with appropriate keywords
3. Run the parser: `python tools/data_extraction/bib_parser.py`
4. Generate updated README: `python tools/data_extraction/readme_generator.py`
5. Submit a pull request

### Keyword Convention

Use these keywords in BibTeX entries:

**Modality**: `CP-LiDAR`, `CP-Camera`, `CP-Fusion`
**Collaboration**: `CP-Early`, `CP-Intermediate`, `CP-Late`, `CP-Hybrid`
**Task**: `CP-Object Detection`, `CP-Object Tracking`, `CP-Semantic Segmentation`, `CP-Motion Prediction`, `CP-Lane Detection`, `CP-Multi-task`

---

## Citation

If you find this repository useful, please cite our survey paper:

```bibtex
@article{wan2026systematic,
  title={A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective},
  author={Wan, Lei and others},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2026}
}
```

---

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International License][cc-by].

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

---

**Maintained by**: [Your Name]
**Last Updated**: 2026-01
**Paper Version**: Accepted for IEEE T-ITS 2026
"""
        return footer

    def generate_full_readme(self, output_path: str):
        """Generate complete README.md file."""
        readme = ""
        readme += self.generate_header()
        readme += self.generate_taxonomy_section()
        readme += self.generate_papers_sections()
        readme += self.generate_tools_section()
        readme += self.generate_footer()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(readme)

        print(f"README generated at: {output_path}")


def main():
    """Main function."""
    data_path = Path(__file__).parent.parent.parent / "data" / "categorized_papers.json"
    output_path = Path(__file__).parent.parent.parent / "README.md"

    print("Generating README from categorized papers...")
    generator = ReadmeGenerator(str(data_path))
    generator.generate_full_readme(str(output_path))
    print("✓ README.md generated successfully!")


if __name__ == "__main__":
    main()
