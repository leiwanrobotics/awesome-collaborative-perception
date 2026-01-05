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
            'Fusion': ['CP-Fusion', 'CP-LiDAR-Camera']
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
            'Motion Prediction': ['CP-Motion Prediction'],
            'Semantic Segmentation': ['CP-Semantic Segmentation'],
            'Lane Detection': ['CP-Lane Detection'],
            'Multi-task': ['CP-Multi-task', 'CP-Task-agnostic']
        }

    def parse_bib_file(self) -> List[Dict[str, Any]]:
        """Parse the entire BibTeX file."""
        with open(self.bib_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by entries (each entry starts with @)
        entries = re.split(r'\n@', content)

        for i, entry in enumerate(entries):
            if not entry.strip():
                continue

            # Add @ back if it's not the first entry
            if i > 0:
                entry = '@' + entry

            parsed_entry = self._parse_entry(entry)
            if parsed_entry:
                self.papers.append(parsed_entry)
                self._categorize_paper(parsed_entry)

        return self.papers

    def _parse_entry(self, entry: str) -> Dict[str, Any]:
        """Parse a single BibTeX entry."""
        try:
            # Extract entry type and citation key
            match = re.match(r'@(\w+)\{([^,]+),', entry)
            if not match:
                return None

            entry_type = match.group(1)
            citation_key = match.group(2)

            paper = {
                'type': entry_type,
                'citation_key': citation_key,
                'fields': {}
            }

            # Extract fields
            field_pattern = r'(\w+)\s*=\s*\{([^}]*)\}'
            for match in re.finditer(field_pattern, entry):
                field_name = match.group(1).lower()
                field_value = match.group(2).strip()
                paper['fields'][field_name] = field_value

            # Extract keywords (special handling as they're crucial)
            keywords_match = re.search(r'keywords\s*=\s*\{([^}]*)\}', entry)
            if keywords_match:
                keywords = [k.strip() for k in keywords_match.group(1).split(',')]
                paper['keywords'] = keywords
            else:
                paper['keywords'] = []

            return paper

        except Exception as e:
            print(f"Error parsing entry: {e}")
            return None

    def _categorize_paper(self, paper: Dict[str, Any]):
        """Categorize a paper based on its keywords."""
        keywords = paper.get('keywords', [])

        # Categorize by modality
        for modality, kw_list in self.modality_keywords.items():
            if any(kw in keywords for kw in kw_list):
                self.categories['modality'][modality].append(paper)

        # Categorize by collaboration type
        for collab_type, kw_list in self.collaboration_keywords.items():
            if any(kw in keywords for kw in kw_list):
                self.categories['collaboration'][collab_type].append(paper)

        # Categorize by task
        for task, kw_list in self.task_keywords.items():
            if any(kw in keywords for kw in kw_list):
                self.categories['task'][task].append(paper)

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
