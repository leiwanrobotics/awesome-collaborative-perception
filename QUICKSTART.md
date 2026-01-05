# Quick Start Guide

Get started with the Awesome Collaborative Perception repository in 5 minutes!

## Prerequisites

- Python 3.8+
- pip

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/awesome-collaborative-perception.git
cd awesome-collaborative-perception

# Install dependencies
pip install -r requirements.txt
```

## Basic Usage

### 1. View the Paper Collection

The main [README.md](README.md) contains all 109 categorized papers organized by:
- Modality (LiDAR, Camera, Fusion)
- Collaboration Type (Early, Intermediate, Late, Hybrid)
- Perception Task (Object Detection, Tracking, Segmentation, etc.)

### 2. Parse BibTeX File

If you have new papers to add:

```bash
# Add entries to collaborative-perception.bib with keywords
# Then run the parser
python tools/data_extraction/bib_parser.py
```

**Output**: `data/categorized_papers.json`

### 3. Generate README

After parsing, regenerate the README:

```bash
python tools/data_extraction/readme_generator.py
```

**Output**: Updated `README.md`

## Advanced Features

### Forward Snowballing

Discover new papers citing existing works:

```bash
# Find all citing papers (takes time due to API rate limits)
python tools/snowballing/forward_snowballing.py

# Test with limited papers
python tools/snowballing/forward_snowballing.py --max-papers 5
```

**Output**: `data/snowballing/new_candidates.json`

### LLM-based Study Selection

Automatically screen new papers:

```bash
# Set your SiliconFlow API key
export SILICONFLOW_API_KEY="your-key-here"

# Run automated screening
python tools/study_selection/llm_classifier.py \
  --candidates data/snowballing/new_candidates.json
```

**Output**:
- `data/study_selection/study_selection_final.json`
- `data/study_selection/selection_summary.md`

## Complete Workflow Example

```bash
# 1. Parse existing papers
python tools/data_extraction/bib_parser.py

# 2. Generate README
python tools/data_extraction/readme_generator.py

# 3. Find new papers (test mode)
python tools/snowballing/forward_snowballing.py --max-papers 3

# 4. Screen new papers (requires API key)
export SILICONFLOW_API_KEY="your-key"
python tools/study_selection/llm_classifier.py

# 5. Review results
cat data/study_selection/selection_summary.md
```

## Project Structure

```
awesome-collaborative-perception/
├── README.md                           # Main paper collection
├── collaborative-perception.bib        # BibTeX database (109 papers)
├── data/
│   ├── categorized_papers.json        # Parsed paper data
│   ├── snowballing/                   # Forward snowballing results
│   └── study_selection/               # LLM screening results
├── tools/
│   ├── data_extraction/               # Parser and generator
│   ├── snowballing/                   # Citation discovery
│   └── study_selection/               # LLM classifier
├── config/
│   └── inclusion_criteria.json        # SLR criteria
├── papers/                            # Organized by category
│   ├── by_modality/
│   ├── by_collaboration/
│   └── by_task/
└── requirements.txt                   # Python dependencies
```

## Configuration

### BibTeX Keywords

Add these keywords to new BibTeX entries:

```bibtex
keywords = {CP-LiDAR, CP-Intermediate, CP-Object Detection}
```

**Available keywords**:
- Modality: `CP-LiDAR`, `CP-Camera`, `CP-Fusion`
- Collaboration: `CP-Early`, `CP-Intermediate`, `CP-Late`, `CP-Hybrid`
- Task: `CP-Object Detection`, `CP-Object Tracking`, `CP-Semantic Segmentation`, `CP-Motion Prediction`, `CP-Lane Detection`, `CP-Multi-task`

### API Keys

For LLM-based tools, get your API key from:
- **SiliconFlow**: https://cloud.siliconflow.cn/

Set it in your environment:
```bash
export SILICONFLOW_API_KEY="sk-..."
```

Or create a `.env` file:
```bash
echo "SILICONFLOW_API_KEY=sk-..." > .env
```

## Troubleshooting

### Import Error: No module named 'bibtexparser'

```bash
pip install -r requirements.txt
```

### API Rate Limit Exceeded

Increase delay between requests:
```bash
python tools/snowballing/forward_snowballing.py --delay 2.0
```

### BibTeX Parsing Errors

Check your BibTeX syntax:
```bash
python -c "import bibtexparser; bibtexparser.load(open('collaborative-perception.bib'))"
```

## Next Steps

1. **Explore the papers**: Browse [README.md](README.md) by category
2. **Contribute**: Add new papers following our [contribution guidelines](README.md#contributing)
3. **Automate**: Set up periodic snowballing to discover new work
4. **Customize**: Modify taxonomy in `config/inclusion_criteria.json`

## Getting Help

- **Documentation**: See [tools/README.md](tools/README.md) for detailed tool usage
- **Survey Paper**: Read the full systematic review in the PDF
- **Issues**: Report problems or ask questions via GitHub Issues

## Citation

```bibtex
@article{wan2026systematic,
  title={A Systematic Literature Review on Vehicular Collaborative Perception: A Computer Vision Perspective},
  author={Wan, Lei and others},
  journal={IEEE Transactions on Intelligent Transportation Systems},
  year={2026}
}
```

---

**Happy researching! 🚗📚**
