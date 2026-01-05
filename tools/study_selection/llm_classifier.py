#!/usr/bin/env python3
"""
LLM-based Study Selection Tool for Collaborative Perception
Uses SiliconFlow API to apply inclusion/exclusion criteria from the systematic review.
"""

import json
import os
import time
import requests
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


class SiliconFlowClassifier:
    """LLM-based classifier using SiliconFlow API."""

    def __init__(self, api_key: Optional[str] = None, model: str = "Qwen/Qwen2.5-72B-Instruct"):
        """
        Initialize the classifier.

        Args:
            api_key: SiliconFlow API key (or set SILICONFLOW_API_KEY env var)
            model: Model to use (default: Qwen2.5-72B-Instruct)
        """
        self.api_key = api_key or os.getenv('SILICONFLOW_API_KEY')
        if not self.api_key:
            raise ValueError("API key required. Set SILICONFLOW_API_KEY or pass api_key parameter.")

        self.api_endpoint = "https://api.siliconflow.cn/v1/chat/completions"
        self.model = model

    def call_llm(self, prompt: str, temperature: float = 0.1, max_tokens: int = 1000) -> str:
        """
        Call SiliconFlow API.

        Args:
            prompt: Prompt for the LLM
            temperature: Sampling temperature
            max_tokens: Maximum tokens in response

        Returns:
            LLM response text
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(self.api_endpoint, headers=headers, json=payload, timeout=60)
            response.raise_for_status()

            data = response.json()
            return data['choices'][0]['message']['content']

        except Exception as e:
            print(f"Error calling LLM API: {e}")
            return ""

    def apply_inclusion_criteria(self, paper: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply inclusion criteria from the systematic review (Table III).

        Inclusion Criteria (IC):
        IC1: Primary study with explicit research character
        IC2: Published between 2019-2024
        IC3: Academic article (conference or journal)
        IC4: Addresses cooperative perception between different entities

        Args:
            paper: Paper metadata

        Returns:
            Classification result with reasoning
        """
        title = paper.get('title', 'N/A')
        authors = paper.get('authors', [])
        year = paper.get('year', 'N/A')
        venue = paper.get('venue', 'N/A')
        abstract = paper.get('abstract', 'N/A')

        authors_str = ', '.join(authors) if isinstance(authors, list) else str(authors)

        prompt = f"""You are an expert in systematic literature review for collaborative perception in autonomous vehicles.

Evaluate the following paper against the INCLUSION criteria:

**Paper Information:**
- Title: {title}
- Authors: {authors_str}
- Year: {year}
- Venue: {venue}
- Abstract: {abstract}

**Inclusion Criteria:**
IC1: The work is a primary study with explicit research character (not a survey, review, or editorial)
IC2: Published between 2019-2024
IC3: Academic article from conference or journal (not grey literature, preprint, or workshop)
IC4: Addresses cooperative perception between different entities (V2V or V2I, not single-vehicle perception)

**Task:**
Evaluate each criterion (IC1-IC4) and provide:
1. A decision for each criterion: PASS or FAIL
2. Brief reasoning for each decision
3. Overall decision: INCLUDE or EXCLUDE

**Output Format (JSON):**
{{
  "ic1": {{"decision": "PASS/FAIL", "reasoning": "..."}},
  "ic2": {{"decision": "PASS/FAIL", "reasoning": "..."}},
  "ic3": {{"decision": "PASS/FAIL", "reasoning": "..."}},
  "ic4": {{"decision": "PASS/FAIL", "reasoning": "..."}},
  "overall": "INCLUDE/EXCLUDE",
  "confidence": "high/medium/low",
  "summary": "Brief summary of decision"
}}

Respond with ONLY the JSON object, no additional text.
"""

        response = self.call_llm(prompt, temperature=0.1)

        try:
            # Extract JSON from response
            result = json.loads(response.strip())
            result['paper_title'] = title
            return result
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails
            return {
                'paper_title': title,
                'overall': 'UNKNOWN',
                'error': 'Failed to parse LLM response',
                'raw_response': response
            }

    def apply_exclusion_criteria(self, paper: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply exclusion criteria from the systematic review (Table III).

        Exclusion Criteria (EC):
        EC1: Not written in English
        EC2: Grey literature (e.g., technical reports, dissertations)
        EC3: Duplicate or extended version of another study
        EC4: Addresses only single-entity perception
        EC5: No details on evaluation method
        EC6: Focuses only on communication protocol design

        Args:
            paper: Paper metadata

        Returns:
            Classification result with reasoning
        """
        title = paper.get('title', 'N/A')
        authors = paper.get('authors', [])
        year = paper.get('year', 'N/A')
        venue = paper.get('venue', 'N/A')
        abstract = paper.get('abstract', 'N/A')

        authors_str = ', '.join(authors) if isinstance(authors, list) else str(authors)

        prompt = f"""You are an expert in systematic literature review for collaborative perception in autonomous vehicles.

Evaluate the following paper against the EXCLUSION criteria:

**Paper Information:**
- Title: {title}
- Authors: {authors_str}
- Year: {year}
- Venue: {venue}
- Abstract: {abstract}

**Exclusion Criteria:**
EC1: Not written in English (check title and abstract language)
EC2: Grey literature (technical report, dissertation, thesis, white paper)
EC3: Duplicate or extended version of another study
EC4: Addresses only single-entity perception (no collaboration)
EC5: No details on evaluation method mentioned
EC6: Focuses only on communication protocol design (no perception)

**Task:**
Evaluate each criterion (EC1-EC6) and provide:
1. A decision for each criterion: TRIGGERED or NOT_TRIGGERED
2. Brief reasoning for each decision
3. Overall decision: EXCLUDE or KEEP

**Output Format (JSON):**
{{
  "ec1": {{"decision": "TRIGGERED/NOT_TRIGGERED", "reasoning": "..."}},
  "ec2": {{"decision": "TRIGGERED/NOT_TRIGGERED", "reasoning": "..."}},
  "ec3": {{"decision": "TRIGGERED/NOT_TRIGGERED", "reasoning": "..."}},
  "ec4": {{"decision": "TRIGGERED/NOT_TRIGGERED", "reasoning": "..."}},
  "ec5": {{"decision": "TRIGGERED/NOT_TRIGGERED", "reasoning": "..."}},
  "ec6": {{"decision": "TRIGGERED/NOT_TRIGGERED", "reasoning": "..."}},
  "overall": "EXCLUDE/KEEP",
  "confidence": "high/medium/low",
  "summary": "Brief summary of decision"
}}

Respond with ONLY the JSON object, no additional text.
"""

        response = self.call_llm(prompt, temperature=0.1)

        try:
            result = json.loads(response.strip())
            result['paper_title'] = title
            return result
        except json.JSONDecodeError:
            return {
                'paper_title': title,
                'overall': 'UNKNOWN',
                'error': 'Failed to parse LLM response',
                'raw_response': response
            }

    def classify_taxonomy(self, paper: Dict[str, Any]) -> Dict[str, Any]:
        """
        Classify a paper according to the collaborative perception taxonomy.

        Taxonomy dimensions:
        1. Modality: LiDAR / Camera / LiDAR-Camera Fusion / Other
        2. Collaboration Type: Early / Intermediate / Late / Hybrid
        3. Perception Task: Object Detection / Object Tracking / Motion Prediction /
                          Semantic Segmentation / Lane Detection / Multi-task

        Args:
            paper: Paper metadata

        Returns:
            Taxonomy classification
        """
        title = paper.get('title', 'N/A')
        abstract = paper.get('abstract', 'N/A')

        prompt = f"""You are an expert in collaborative perception for autonomous vehicles.

Classify the following paper according to the collaborative perception taxonomy:

**Paper Information:**
- Title: {title}
- Abstract: {abstract}

**Taxonomy Dimensions:**

1. **Modality** (select all that apply):
   - LiDAR: Uses 3D point cloud data
   - Camera: Uses 2D RGB images
   - Fusion: Combines LiDAR and Camera
   - Other: Other sensors (radar, etc.)

2. **Collaboration Type** (select primary type):
   - Early: Shares raw sensor data (point clouds, images)
   - Intermediate: Shares intermediate feature representations
   - Late: Shares detection/prediction results
   - Hybrid: Combines multiple collaboration strategies

3. **Perception Task** (select all that apply):
   - Object Detection: 3D bounding box detection
   - Object Tracking: Multi-object tracking over time
   - Motion Prediction: Future trajectory forecasting
   - Semantic Segmentation: Point-wise or pixel-wise classification
   - Lane Detection: Road structure understanding
   - Multi-task: Multiple perception tasks

**Output Format (JSON):**
{{
  "modality": ["LiDAR", "Camera", ...],
  "collaboration_type": "Early/Intermediate/Late/Hybrid",
  "perception_tasks": ["Object Detection", ...],
  "confidence": "high/medium/low",
  "reasoning": "Brief explanation of classification"
}}

Respond with ONLY the JSON object, no additional text.
"""

        response = self.call_llm(prompt, temperature=0.1)

        try:
            result = json.loads(response.strip())
            result['paper_title'] = title
            return result
        except json.JSONDecodeError:
            return {
                'paper_title': title,
                'error': 'Failed to parse LLM response',
                'raw_response': response
            }


class StudySelectionPipeline:
    """Complete study selection pipeline."""

    def __init__(self, classifier: SiliconFlowClassifier, output_dir: str = "data/study_selection"):
        self.classifier = classifier
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_candidates(self, candidates_path: str, delay: float = 1.0) -> Dict[str, Any]:
        """
        Process all candidate papers through the selection pipeline.

        Args:
            candidates_path: Path to candidates JSON file
            delay: Delay between API calls (seconds)

        Returns:
            Processing results
        """
        with open(candidates_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        candidates = data.get('candidates', [])

        results = {
            'total_processed': 0,
            'included': [],
            'excluded': [],
            'uncertain': [],
            'taxonomy_classified': [],
            'timestamp': datetime.now().isoformat()
        }

        print(f"\nProcessing {len(candidates)} candidate papers...\n")

        for i, paper in enumerate(candidates, 1):
            print(f"[{i}/{len(candidates)}] {paper.get('title', 'Untitled')[:60]}...")

            # Apply inclusion criteria
            print("  Checking inclusion criteria...")
            inclusion_result = self.classifier.apply_inclusion_criteria(paper)
            time.sleep(delay)

            # Apply exclusion criteria
            print("  Checking exclusion criteria...")
            exclusion_result = self.classifier.apply_exclusion_criteria(paper)
            time.sleep(delay)

            # Determine final decision
            included = (inclusion_result.get('overall') == 'INCLUDE' and
                       exclusion_result.get('overall') == 'KEEP')

            paper_result = {
                'paper': paper,
                'inclusion_analysis': inclusion_result,
                'exclusion_analysis': exclusion_result,
                'final_decision': 'INCLUDED' if included else 'EXCLUDED'
            }

            if included:
                print("  ✓ INCLUDED - Classifying taxonomy...")
                # Classify taxonomy for included papers
                taxonomy = self.classifier.classify_taxonomy(paper)
                time.sleep(delay)

                paper_result['taxonomy'] = taxonomy
                results['included'].append(paper_result)
                results['taxonomy_classified'].append(taxonomy)
            else:
                print("  ✗ EXCLUDED")
                results['excluded'].append(paper_result)

            results['total_processed'] += 1

            # Save checkpoint every 10 papers
            if i % 10 == 0:
                self._save_results(results, suffix=f"_checkpoint_{i}")

        return results

    def _save_results(self, results: Dict[str, Any], suffix: str = ""):
        """Save processing results."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"study_selection_{timestamp}{suffix}.json"
        output_path = self.output_dir / filename

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"  Results saved to: {output_path}")

    def generate_summary_report(self, results: Dict[str, Any], output_path: str):
        """Generate a summary report of the selection process."""
        report = f"""# Study Selection Summary Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Overview

- **Total Candidates Processed:** {results['total_processed']}
- **Included:** {len(results['included'])}
- **Excluded:** {len(results['excluded'])}
- **Inclusion Rate:** {len(results['included'])/results['total_processed']*100:.1f}%

## Included Papers by Taxonomy

"""

        # Count by modality
        modality_counts = {}
        for taxonomy in results['taxonomy_classified']:
            for mod in taxonomy.get('modality', []):
                modality_counts[mod] = modality_counts.get(mod, 0) + 1

        report += "### By Modality\n\n"
        for mod, count in sorted(modality_counts.items()):
            report += f"- {mod}: {count}\n"

        # Count by collaboration type
        collab_counts = {}
        for taxonomy in results['taxonomy_classified']:
            collab = taxonomy.get('collaboration_type', 'Unknown')
            collab_counts[collab] = collab_counts.get(collab, 0) + 1

        report += "\n### By Collaboration Type\n\n"
        for collab, count in sorted(collab_counts.items()):
            report += f"- {collab}: {count}\n"

        # Count by task
        task_counts = {}
        for taxonomy in results['taxonomy_classified']:
            for task in taxonomy.get('perception_tasks', []):
                task_counts[task] = task_counts.get(task, 0) + 1

        report += "\n### By Perception Task\n\n"
        for task, count in sorted(task_counts.items()):
            report += f"- {task}: {count}\n"

        report += "\n## Included Papers\n\n"
        for item in results['included']:
            paper = item['paper']
            report += f"### {paper.get('title', 'Untitled')}\n\n"
            report += f"- **Authors:** {', '.join(paper.get('authors', []))}\n"
            report += f"- **Year:** {paper.get('year', 'N/A')}\n"
            report += f"- **Venue:** {paper.get('venue', 'N/A')}\n"

            taxonomy = item.get('taxonomy', {})
            report += f"- **Modality:** {', '.join(taxonomy.get('modality', []))}\n"
            report += f"- **Collaboration:** {taxonomy.get('collaboration_type', 'N/A')}\n"
            report += f"- **Tasks:** {', '.join(taxonomy.get('perception_tasks', []))}\n\n"

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"\nSummary report saved to: {output_path}")


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(description='LLM-based study selection tool')
    parser.add_argument('--candidates', type=str,
                       default='data/snowballing/new_candidates.json',
                       help='Path to candidates JSON')
    parser.add_argument('--api-key', type=str,
                       help='SiliconFlow API key (or set SILICONFLOW_API_KEY env var)')
    parser.add_argument('--model', type=str,
                       default='Qwen/Qwen2.5-72B-Instruct',
                       help='Model to use')
    parser.add_argument('--output-dir', type=str,
                       default='data/study_selection',
                       help='Output directory')
    parser.add_argument('--delay', type=float, default=1.0,
                       help='Delay between API calls (seconds)')

    args = parser.parse_args()

    # Initialize classifier
    classifier = SiliconFlowClassifier(api_key=args.api_key, model=args.model)

    # Initialize pipeline
    pipeline = StudySelectionPipeline(classifier, output_dir=args.output_dir)

    print("=" * 60)
    print("LLM-BASED STUDY SELECTION TOOL")
    print("=" * 60)

    # Process candidates
    results = pipeline.process_candidates(args.candidates, delay=args.delay)

    # Save final results
    pipeline._save_results(results, suffix="_final")

    # Generate summary report
    report_path = Path(args.output_dir) / "selection_summary.md"
    pipeline.generate_summary_report(results, str(report_path))

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total processed: {results['total_processed']}")
    print(f"Included: {len(results['included'])}")
    print(f"Excluded: {len(results['excluded'])}")
    print(f"Inclusion rate: {len(results['included'])/results['total_processed']*100:.1f}%")
    print("=" * 60)


if __name__ == "__main__":
    main()
