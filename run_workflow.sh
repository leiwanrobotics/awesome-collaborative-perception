#!/bin/bash
# Master workflow script for awesome-collaborative-perception
# Automates the complete systematic review workflow

set -e  # Exit on error

echo "=================================="
echo "Awesome Collaborative Perception"
echo "Automated Workflow Script"
echo "=================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print section headers
print_section() {
    echo ""
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
    echo ""
}

# Function to print success messages
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Function to print warnings
print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

print_success "Python 3 found"

# Check if dependencies are installed
print_section "Checking Dependencies"

if python3 -c "import bibtexparser" 2>/dev/null; then
    print_success "bibtexparser installed"
else
    print_warning "Installing bibtexparser..."
    pip install bibtexparser
fi

if python3 -c "import requests" 2>/dev/null; then
    print_success "requests installed"
else
    print_warning "Installing requests..."
    pip install requests
fi

# Parse command line arguments
MODE=${1:-full}

case $MODE in
    parse)
        print_section "Step 1: Parsing BibTeX File"
        python3 tools/data_extraction/bib_parser.py
        print_success "BibTeX parsing completed"

        print_section "Step 2: Generating README"
        python3 tools/data_extraction/readme_generator.py
        print_success "README generation completed"
        ;;

    snowball)
        print_section "Forward Snowballing"

        # Ask for number of papers to process
        read -p "Enter max papers to process (or press Enter for all): " max_papers

        if [ -z "$max_papers" ]; then
            python3 tools/snowballing/forward_snowballing.py
        else
            python3 tools/snowballing/forward_snowballing.py --max-papers "$max_papers"
        fi

        print_success "Forward snowballing completed"
        ;;

    classify)
        print_section "LLM-based Study Selection"

        # Check for API key
        if [ -z "$SILICONFLOW_API_KEY" ]; then
            print_warning "SILICONFLOW_API_KEY not set"
            read -p "Enter your SiliconFlow API key: " api_key
            export SILICONFLOW_API_KEY="$api_key"
        fi

        python3 tools/study_selection/llm_classifier.py
        print_success "Study selection completed"

        echo ""
        echo "Review the results in:"
        echo "  - data/study_selection/study_selection_final.json"
        echo "  - data/study_selection/selection_summary.md"
        ;;

    full)
        print_section "Step 1: Parsing BibTeX File"
        python3 tools/data_extraction/bib_parser.py
        print_success "BibTeX parsing completed"

        print_section "Step 2: Generating README"
        python3 tools/data_extraction/readme_generator.py
        print_success "README generation completed"

        print_section "Step 3: Forward Snowballing (Test Mode)"
        print_warning "Running in test mode with 5 papers (use ./run_workflow.sh snowball for full run)"
        python3 tools/snowballing/forward_snowballing.py --max-papers 5
        print_success "Forward snowballing completed"

        echo ""
        print_warning "Skipping LLM classification (requires API key)"
        echo "To run classification: ./run_workflow.sh classify"
        ;;

    help)
        echo "Usage: ./run_workflow.sh [MODE]"
        echo ""
        echo "Modes:"
        echo "  parse      - Parse BibTeX and generate README only"
        echo "  snowball   - Run forward snowballing to find new papers"
        echo "  classify   - Run LLM-based study selection (requires API key)"
        echo "  full       - Run complete workflow (default, test mode for snowballing)"
        echo "  help       - Show this help message"
        echo ""
        echo "Examples:"
        echo "  ./run_workflow.sh              # Run full workflow"
        echo "  ./run_workflow.sh parse        # Just parse and generate README"
        echo "  ./run_workflow.sh snowball     # Find citing papers"
        echo "  ./run_workflow.sh classify     # Classify new candidates"
        ;;

    *)
        echo "Unknown mode: $MODE"
        echo "Use './run_workflow.sh help' for usage information"
        exit 1
        ;;
esac

echo ""
print_section "Workflow Complete!"

# Show summary
echo "Generated files:"
if [ -f "data/categorized_papers.json" ]; then
    echo "  ✓ data/categorized_papers.json"
fi
if [ -f "README.md" ]; then
    echo "  ✓ README.md"
fi
if [ -d "data/snowballing" ] && [ "$(ls -A data/snowballing)" ]; then
    echo "  ✓ data/snowballing/"
fi
if [ -d "data/study_selection" ] && [ "$(ls -A data/study_selection)" ]; then
    echo "  ✓ data/study_selection/"
fi

echo ""
echo "For detailed documentation, see:"
echo "  - QUICKSTART.md"
echo "  - tools/README.md"
echo ""
