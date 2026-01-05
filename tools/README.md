# Automated Tools for Systematic Literature Review

This directory contains automated tools for managing and extending the collaborative perception paper collection.

## Overview

The toolset includes three main components:

1. **BibTeX Parser** - Categorize papers from BibTeX files
2. **Forward Snowballing** - Discover new papers citing existing works
3. **LLM-based Study Selection** - Automated paper classification and filtering

## Directory Structure

```
tools/
├── data_extraction/
│   ├── bib_parser.py          # Parse and categorize BibTeX entries
│   └── readme_generator.py    # Generate README from categorized papers
├── snowballing/
│   └── forward_snowballing.py # Find citing papers via APIs
├── study_selection/
│   └── llm_classifier.py      # LLM-based inclusion/exclusion screening
└── README.md                  # This file
```

---

## 1. BibTeX Parser

Parses BibTeX files and categorizes papers based on keywords following the taxonomy from the systematic review.

### Usage

```bash
# Basic usage
python tools/data_extraction/bib_parser.py

# Output: data/categorized_papers.json
```

### Keyword Convention

Papers are categorized using these keywords in BibTeX entries:

**Modality:**
- `CP-LiDAR` - LiDAR-based methods
- `CP-Camera` - Camera-based methods
- `CP-Fusion` or `CP-LiDAR-Camera` - Multi-modal fusion

**Collaboration Type:**
- `CP-Early` - Early collaboration (raw data sharing)
- `CP-Intermediate` - Intermediate collaboration (feature sharing)
- `CP-Late` - Late collaboration (result sharing)
- `CP-Hybrid` - Hybrid collaboration

**Perception Task:**
- `CP-Object Detection` - 3D object detection
- `CP-Object Tracking` - Multi-object tracking
- `CP-Semantic Segmentation` - Point/pixel-wise segmentation
- `CP-Motion Prediction` - Trajectory forecasting
- `CP-Lane Detection` - Lane/road detection
- `CP-Multi-task` - Multiple tasks

### Example BibTeX Entry

```bibtex
@inproceedings{example2024,
  title = {Example Paper on Collaborative Perception},
  author = {Smith, John and Doe, Jane},
  booktitle = {IEEE Intelligent Vehicles Symposium (IV)},
  year = {2024},
  doi = {10.1109/example.2024.12345},
  keywords = {CP-LiDAR, CP-Intermediate, CP-Object Detection},
}
```

---

## 2. README Generator

Automatically generates the repository README from categorized papers.

### Usage

```bash
python tools/data_extraction/readme_generator.py

# Output: README.md
```

The generator creates:
- Statistics table
- Taxonomy overview
- Categorized paper listings with formatted citations
- Contribution guidelines

---

## 3. Forward Snowballing Tool

Discovers new papers that cite existing works using academic APIs.

### Features

- **Semantic Scholar API**: Comprehensive citation data with abstracts
- **OpenCitations API**: Citation index from multiple sources
- **Deduplication**: Removes duplicate papers across sources
- **Checkpoint saving**: Saves progress every 10 papers

### Setup

No API keys required for basic usage (uses public APIs with rate limiting).

### Usage

```bash
# Process all papers
python tools/snowballing/forward_snowballing.py

# Process limited number (for testing)
python tools/snowballing/forward_snowballing.py --max-papers 10

# Custom output directory
python tools/snowballing/forward_snowballing.py --output-dir my_results/

# Output: data/snowballing/new_candidates.json
```

### Output Format

```json
{
  "total_unique_candidates": 150,
  "candidates": [
    {
      "title": "Paper Title",
      "authors": ["Author 1", "Author 2"],
      "year": 2024,
      "venue": "Conference/Journal Name",
      "abstract": "Paper abstract...",
      "source": "Semantic Scholar"
    }
  ],
  "generation_date": "2026-01-05T10:30:00"
}
```

---

## 4. LLM-based Study Selection

Uses SiliconFlow LLM API to automatically apply inclusion/exclusion criteria and classify papers by taxonomy.

### Features

- **Inclusion Criteria Checking** (IC1-IC4)
- **Exclusion Criteria Checking** (EC1-EC6)
- **Taxonomy Classification** (Modality, Collaboration Type, Tasks)
- **Confidence Scoring**
- **Detailed Reasoning**

### Setup

Set your SiliconFlow API key:

```bash
export SILICONFLOW_API_KEY="your-api-key-here"
```

Or pass it as an argument:

```bash
python tools/study_selection/llm_classifier.py --api-key "your-api-key"
```

### Usage

```bash
# Process candidates from snowballing
python tools/study_selection/llm_classifier.py \
  --candidates data/snowballing/new_candidates.json

# Use different model
python tools/study_selection/llm_classifier.py \
  --model "Qwen/Qwen2.5-72B-Instruct"

# Adjust API rate limiting
python tools/study_selection/llm_classifier.py --delay 2.0

# Output: data/study_selection/study_selection_final.json
#         data/study_selection/selection_summary.md
```

### Inclusion Criteria (from Table III)

- **IC1**: Primary study with explicit research character
- **IC2**: Published 2019-2024
- **IC3**: Academic article (conference/journal)
- **IC4**: Addresses cooperative perception between entities

### Exclusion Criteria (from Table III)

- **EC1**: Not written in English
- **EC2**: Grey literature
- **EC3**: Duplicate/extended version
- **EC4**: Single-entity perception only
- **EC5**: No evaluation details
- **EC6**: Communication protocol design only

### Output Format

```json
{
  "total_processed": 100,
  "included": [
    {
      "paper": { ... },
      "inclusion_analysis": {
        "ic1": {"decision": "PASS", "reasoning": "..."},
        "ic2": {"decision": "PASS", "reasoning": "..."},
        "overall": "INCLUDE"
      },
      "exclusion_analysis": {
        "ec1": {"decision": "NOT_TRIGGERED", "reasoning": "..."},
        "overall": "KEEP"
      },
      "taxonomy": {
        "modality": ["LiDAR"],
        "collaboration_type": "Intermediate",
        "perception_tasks": ["Object Detection"]
      }
    }
  ],
  "excluded": [ ... ]
}
```

---

## Complete Workflow

### 1. Initial Setup

```bash
# Parse existing BibTeX file
python tools/data_extraction/bib_parser.py

# Generate initial README
python tools/data_extraction/readme_generator.py
```

### 2. Discover New Papers

```bash
# Run forward snowballing
python tools/snowballing/forward_snowballing.py

# Output: data/snowballing/new_candidates.json
```

### 3. Filter and Classify

```bash
# Apply inclusion/exclusion criteria
export SILICONFLOW_API_KEY="your-key"
python tools/study_selection/llm_classifier.py

# Review results: data/study_selection/selection_summary.md
```

### 4. Add to Repository

For papers that pass screening:

1. Add BibTeX entry to `collaborative-perception.bib`
2. Include appropriate keywords (CP-LiDAR, CP-Intermediate, etc.)
3. Re-run parser and generator:

```bash
python tools/data_extraction/bib_parser.py
python tools/data_extraction/readme_generator.py
```

---

## API Rate Limits

### Semantic Scholar API
- **Rate Limit**: 100 requests/5 minutes (public API)
- **Recommendation**: Use `--delay 1.0` or higher
- **Documentation**: https://api.semanticscholar.org/

### OpenCitations API
- **Rate Limit**: Generally lenient for reasonable use
- **Documentation**: https://opencitations.net/

### SiliconFlow API
- **Rate Limit**: Depends on your plan
- **Recommendation**: Use `--delay 1.0` to avoid issues
- **Documentation**: https://cloud.siliconflow.cn/

---

## Troubleshooting

### Issue: API rate limit exceeded

**Solution**: Increase delay between requests:
```bash
python tools/snowballing/forward_snowballing.py --delay 2.0
```

### Issue: LLM parsing errors

**Solution**: Check API key and model availability:
```bash
# Verify API key is set
echo $SILICONFLOW_API_KEY

# Try different model
python tools/study_selection/llm_classifier.py --model "another-model"
```

### Issue: BibTeX parsing errors

**Solution**: Check BibTeX file syntax:
```bash
# Validate BibTeX file
bibtex -terse collaborative-perception.bib
```

---

## Contributing

When adding new tools or features:

1. Follow existing code structure
2. Include docstrings and type hints
3. Add error handling and logging
4. Update this README
5. Test with sample data before full run

---

## Dependencies

```bash
# Required Python packages
pip install requests bibtexparser

# Optional (for BibTeX validation)
sudo apt-get install bibtex2html
```

---

## Citation

If you use these tools in your research, please cite our survey paper:

```bibtex
@article{wan2026systematic,
  title={A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective},
  author={Wan, Lei and others},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2026}
}
```
