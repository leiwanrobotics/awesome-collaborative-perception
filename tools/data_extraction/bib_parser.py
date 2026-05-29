#!/usr/bin/env python3
"""
BibTeX Parser for Collaborative Perception Papers
Parses and categorizes papers based on keywords from the systematic literature review.
"""

import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Any


class BibTeXParser:
    """Parser for collaborative perception BibTeX file."""

    def __init__(self, bib_path: str):
        self.bib_path = Path(bib_path)
        self.papers = []
        self.categories = {
            'modality': defaultdict(list),
            'collaboration': defaultdict(list),
            'task': defaultdict(list)
        }

        # Keyword mapping based on survey taxonomy
        self.modality_keywords = {
            'LiDAR': ['CP-LiDAR'],
            'Camera': ['CP-Camera'],
            'LiDAR-Camera': ['CP-Fusion', 'CP-LiDAR-Camera']
        }

        self.collaboration_keywords = {
            'Early': ['CP-Early'],
            'Intermediate': ['CP-Intermediate', 'CP-Intermeidate'],  # Handle typo in original
            'Late': ['CP-Late'],
            'Hybrid': ['CP-Hybrid']
        }

        self.task_keywords = {
            'Object Detection': ['CP-Object Detection'],
            'Object Tracking': ['CP-Object Tracking'],
            'Motion Prediction': ['CP-Motion Prediction', 'CP-Prediction'],
            'Semantic Segmentation': ['CP-Semantic Segmentation'],
            'Lane Detection': ['CP-Lane Detection'],
            'Multi-Task & Task-Agnostic': ['CP-Multi-task', 'CP-Task-agnostic', 'CP-Task Agnostic']
        }

    def parse_bib_file(self) -> List[Dict[str, Any]]:
        """Parse the entire BibTeX file using the bibtexparser library.

        bibtexparser correctly handles nested braces (e.g. ``{2023 {IEEE}/{CVF} ICCV}``),
        which the previous brace-naive regex truncated, corrupting ~half of all venues.
        """
        import bibtexparser
        from bibtexparser.bparser import BibTexParser

        parser = BibTexParser(common_strings=True)
        parser.ignore_nonstandard_types = False
        with open(self.bib_path, 'r', encoding='utf-8') as f:
            db = bibtexparser.load(f, parser=parser)

        for entry in db.entries:
            paper = self._convert_entry(entry)
            self.papers.append(paper)
            self._categorize_paper(paper)

        return self.papers

    def _convert_entry(self, entry: Dict[str, str]) -> Dict[str, Any]:
        """Convert a bibtexparser entry dict to the internal paper structure."""
        citation_key = entry.get('ID', '')
        entry_type = entry.get('ENTRYTYPE', '')

        fields = {k.lower(): re.sub(r'\s+', ' ', v).strip()
                  for k, v in entry.items()
                  if k not in ('ID', 'ENTRYTYPE')}

        keywords_raw = fields.get('keywords', '')
        keywords = [k.strip() for k in keywords_raw.split(',') if k.strip()]

        return {
            'type': entry_type,
            'citation_key': citation_key,
            'fields': fields,
            'keywords': keywords,
        }

    def _categorize_paper(self, paper: Dict[str, Any]):
        """Categorize a paper based on its keywords."""
        keywords = set(paper.get('keywords', []))

        modality = self._infer_modality(keywords)
        if modality:
            self.categories['modality'][modality].append(paper)

        collaboration = self._infer_collaboration(keywords)
        if collaboration:
            self.categories['collaboration'][collaboration].append(paper)

        task = self._infer_task(keywords)
        if task:
            self.categories['task'][task].append(paper)

    def _infer_modality(self, keywords: set) -> str:
        """Infer the primary modality from keywords."""
        has_lidar = 'CP-LiDAR' in keywords
        has_camera = 'CP-Camera' in keywords

        if 'CP-Fusion' in keywords or 'CP-LiDAR-Camera' in keywords or (has_lidar and has_camera):
            return 'LiDAR-Camera'
        if has_lidar:
            return 'LiDAR'
        if has_camera:
            return 'Camera'
        return ''

    def _infer_collaboration(self, keywords: set) -> str:
        """Infer collaboration type from keywords."""
        for collab_type, kw_list in self.collaboration_keywords.items():
            if any(kw in keywords for kw in kw_list):
                return collab_type
        return ''

    def _infer_task(self, keywords: set) -> str:
        """Infer the primary perception task from keywords."""
        for task, kw_list in self.task_keywords.items():
            if any(kw in keywords for kw in kw_list):
                return task
        return ''

    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about the parsed papers."""
        stats = {
            'total_papers': len(self.papers),
            'by_modality': {k: len(v) for k, v in self.categories['modality'].items()},
            'by_collaboration': {k: len(v) for k, v in self.categories['collaboration'].items()},
            'by_task': {k: len(v) for k, v in self.categories['task'].items()}
        }
        return stats

    def export_categorized_papers(self, output_path: str):
        """Export categorized papers to JSON."""
        output_data = {
            'papers': self.papers,
            'categories': {
                'modality': {k: [p['citation_key'] for p in v]
                            for k, v in self.categories['modality'].items()},
                'collaboration': {k: [p['citation_key'] for p in v]
                                 for k, v in self.categories['collaboration'].items()},
                'task': {k: [p['citation_key'] for p in v]
                        for k, v in self.categories['task'].items()}
            },
            'statistics': self.get_statistics()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

    def format_paper_markdown(self, paper: Dict[str, Any]) -> str:
        """Format a paper entry as markdown."""
        fields = paper['fields']

        # Extract common fields
        title = fields.get('title', 'Untitled').replace('{', '').replace('}', '')
        author = fields.get('author', 'Unknown')
        year = fields.get('year', 'N/A')
        venue = fields.get('booktitle') or fields.get('journal', 'N/A')
        doi = fields.get('doi', '')

        # Format markdown
        md = f"- **{title}**  \n"
        md += f"  {author}  \n"
        md += f"  *{venue}*, {year}"

        if doi:
            md += f"  \n  DOI: [{doi}](https://doi.org/{doi})"

        md += "\n"

        return md


def main():
    """Main function to parse and categorize papers."""
    bib_path = Path(__file__).parent.parent.parent / "collaborative-perception.bib"
    output_path = Path(__file__).parent.parent.parent / "data" / "categorized_papers.json"

    print(f"Parsing BibTeX file: {bib_path}")
    parser = BibTeXParser(str(bib_path))
    papers = parser.parse_bib_file()

    print(f"\nParsed {len(papers)} papers")

    # Print statistics
    stats = parser.get_statistics()
    print("\n=== Statistics ===")
    print(f"Total papers: {stats['total_papers']}")

    print("\nBy Modality:")
    for modality, count in stats['by_modality'].items():
        print(f"  {modality}: {count}")

    print("\nBy Collaboration Type:")
    for collab, count in stats['by_collaboration'].items():
        print(f"  {collab}: {count}")

    print("\nBy Task:")
    for task, count in stats['by_task'].items():
        print(f"  {task}: {count}")

    # Export to JSON
    parser.export_categorized_papers(str(output_path))
    print(f"\nCategorized papers exported to: {output_path}")


if __name__ == "__main__":
    main()
