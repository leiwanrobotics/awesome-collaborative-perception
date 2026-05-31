#!/usr/bin/env python3
"""
Forward Snowballing Tool for Collaborative Perception Papers
Automatically discovers papers that cite existing works using multiple APIs.
"""

import json
import time
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime


class ForwardSnowballingTool:
    """Tool for finding papers that cite existing works."""

    def __init__(self, output_dir: str = "data/snowballing"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # API endpoints
        self.semantic_scholar_api = "https://api.semanticscholar.org/graph/v1"
        self.opencitations_api = "https://opencitations.net/index/api/v1"

        # Rate limiting
        self.request_delay = 1  # seconds between requests

    def get_semantic_scholar_citations(self, doi: str) -> List[Dict[str, Any]]:
        """
        Get citing papers from Semantic Scholar API.

        Args:
            doi: DOI of the paper

        Returns:
            List of citing papers with metadata
        """
        try:
            # Search for paper by DOI
            search_url = f"{self.semantic_scholar_api}/paper/DOI:{doi}"
            params = {
                'fields': 'title,authors,year,citationCount,citations,citations.title,citations.authors,citations.year,citations.abstract,citations.venue,citations.publicationDate'
            }

            response = requests.get(search_url, params=params, timeout=30)
            time.sleep(self.request_delay)

            if response.status_code != 200:
                print(f"  Error fetching citations for DOI {doi}: {response.status_code}")
                return []

            data = response.json()

            # Extract citing papers
            citations = data.get('citations', [])
            citing_papers = []

            for citation in citations:
                paper_info = {
                    'title': citation.get('title', 'N/A'),
                    'authors': [a.get('name', 'Unknown') for a in citation.get('authors', [])],
                    'year': citation.get('year'),
                    'venue': citation.get('venue', 'N/A'),
                    'abstract': citation.get('abstract', ''),
                    'publication_date': citation.get('publicationDate', ''),
                    'source': 'Semantic Scholar'
                }
                citing_papers.append(paper_info)

            print(f"  Found {len(citing_papers)} citations via Semantic Scholar")
            return citing_papers

        except (requests.RequestException, ValueError) as e:
            print(f"  Error with Semantic Scholar API: {e}")
            return []

    def get_opencitations_citations(self, doi: str) -> List[Dict[str, Any]]:
        """
        Get citing papers from OpenCitations API.

        Args:
            doi: DOI of the paper

        Returns:
            List of citing DOIs
        """
        try:
            url = f"{self.opencitations_api}/citations/{doi}"
            response = requests.get(url, timeout=30)
            time.sleep(self.request_delay)

            if response.status_code != 200:
                print(f"  OpenCitations API error for {doi}: {response.status_code}")
                return []

            data = response.json()
            citing_dois = [item.get('citing') for item in data if 'citing' in item]

            print(f"  Found {len(citing_dois)} citations via OpenCitations")
            return citing_dois

        except (requests.RequestException, ValueError) as e:
            print(f"  Error with OpenCitations API: {e}")
            return []

    def search_arxiv_citations(self, arxiv_id: str) -> List[Dict[str, Any]]:
        """
        Search for papers citing an arXiv paper.

        Note: arXiv doesn't have a direct citation API, so this uses Semantic Scholar.

        Args:
            arxiv_id: arXiv ID

        Returns:
            List of citing papers
        """
        try:
            search_url = f"{self.semantic_scholar_api}/paper/arXiv:{arxiv_id}"
            params = {
                'fields': 'citations,citations.title,citations.authors,citations.year,citations.abstract,citations.venue'
            }

            response = requests.get(search_url, params=params, timeout=30)
            time.sleep(self.request_delay)

            if response.status_code != 200:
                return []

            data = response.json()
            citations = data.get('citations', [])

            citing_papers = []
            for citation in citations:
                paper_info = {
                    'title': citation.get('title', 'N/A'),
                    'authors': [a.get('name', 'Unknown') for a in citation.get('authors', [])],
                    'year': citation.get('year'),
                    'venue': citation.get('venue', 'N/A'),
                    'abstract': citation.get('abstract', ''),
                    'source': 'Semantic Scholar (arXiv)'
                }
                citing_papers.append(paper_info)

            return citing_papers

        except (requests.RequestException, ValueError) as e:
            print(f"  Error searching arXiv citations: {e}")
            return []

    def forward_snowball_from_bib(self, bib_data_path: str, max_papers: Optional[int] = None) -> Dict[str, Any]:
        """
        Perform forward snowballing on all papers in the BibTeX data.

        Args:
            bib_data_path: Path to categorized_papers.json
            max_papers: Maximum number of papers to process (for testing)

        Returns:
            Dictionary containing all discovered citing papers
        """
        with open(bib_data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        papers = data['papers']
        if max_papers:
            papers = papers[:max_papers]

        results = {
            'processed_papers': [],
            'citing_papers': [],
            'summary': {
                'total_processed': 0,
                'total_citations_found': 0,
                'papers_with_citations': 0,
                'timestamp': datetime.now().isoformat()
            }
        }

        print(f"\nProcessing {len(papers)} papers for forward snowballing...\n")

        for i, paper in enumerate(papers, 1):
            citation_key = paper['citation_key']
            fields = paper['fields']
            doi = fields.get('doi', '')
            arxiv = fields.get('eprint', '')

            print(f"[{i}/{len(papers)}] {citation_key}")

            citing_papers = []

            # Try DOI first
            if doi:
                print(f"  Searching by DOI: {doi}")
                citing_papers.extend(self.get_semantic_scholar_citations(doi))

            # Try arXiv if no DOI or no citations found
            elif arxiv:
                print(f"  Searching by arXiv: {arxiv}")
                citing_papers.extend(self.search_arxiv_citations(arxiv))

            # Record results
            paper_result = {
                'citation_key': citation_key,
                'doi': doi,
                'arxiv': arxiv,
                'num_citations': len(citing_papers),
                'citing_papers': citing_papers
            }

            results['processed_papers'].append(paper_result)
            results['citing_papers'].extend(citing_papers)

            if citing_papers:
                results['summary']['papers_with_citations'] += 1

            results['summary']['total_processed'] += 1
            results['summary']['total_citations_found'] += len(citing_papers)

            print(f"  Total citations: {len(citing_papers)}\n")

            # Save intermediate results every 10 papers
            if i % 10 == 0:
                self._save_results(results, suffix=f"_checkpoint_{i}")

        return results

    def _save_results(self, results: Dict[str, Any], suffix: str = "") -> None:
        """Save snowballing results to JSON."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"forward_snowballing_{timestamp}{suffix}.json"
        output_path = self.output_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"Results saved to: {output_path}")

    def export_new_candidates(self, results: Dict[str, Any], output_path: str) -> None:
        """
        Export unique new paper candidates for review.

        Args:
            results: Snowballing results
            output_path: Where to save the candidates
        """
        # Deduplicate citing papers by title
        unique_papers = {}
        for paper in results['citing_papers']:
            title = paper.get('title', '').lower().strip()
            if title and title not in unique_papers:
                unique_papers[title] = paper

        candidates = {
            'total_unique_candidates': len(unique_papers),
            'candidates': list(unique_papers.values()),
            'generation_date': datetime.now().isoformat()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(candidates, f, indent=2, ensure_ascii=False)

        print(f"\nExported {len(unique_papers)} unique candidates to: {output_path}")


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description='Forward snowballing tool')
    parser.add_argument('--bib-data', type=str,
                       default='data/categorized_papers.json',
                       help='Path to categorized papers JSON')
    parser.add_argument('--max-papers', type=int, default=None,
                       help='Maximum papers to process (for testing)')
    parser.add_argument('--output-dir', type=str,
                       default='data/snowballing',
                       help='Output directory for results')

    args = parser.parse_args()

    tool = ForwardSnowballingTool(output_dir=args.output_dir)

    print("=" * 60)
    print("FORWARD SNOWBALLING TOOL")
    print("=" * 60)

    # Perform forward snowballing
    results = tool.forward_snowball_from_bib(args.bib_data, max_papers=args.max_papers)

    # Save final results
    tool._save_results(results, suffix="_final")

    # Export candidates
    candidates_path = Path(args.output_dir) / "new_candidates.json"
    tool.export_new_candidates(results, str(candidates_path))

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total papers processed: {results['summary']['total_processed']}")
    print(f"Papers with citations: {results['summary']['papers_with_citations']}")
    print(f"Total citations found: {results['summary']['total_citations_found']}")
    unique_titles = {p.get('title', '').lower().strip() for p in results['citing_papers']}
    unique_titles.discard('')
    print(f"Unique new candidates: {len(unique_titles)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
