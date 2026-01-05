#!/usr/bin/env python3
"""
Interactive tool to add new papers to the BibTeX database.
Helps generate properly formatted BibTeX entries with correct keywords.
"""

import sys
from pathlib import Path


def print_header():
    """Print tool header."""
    print("=" * 60)
    print("Add New Paper to Collaborative Perception Database")
    print("=" * 60)
    print()


def get_input(prompt, required=True):
    """Get user input with optional requirement."""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("  ⚠ This field is required. Please provide a value.")


def select_keywords():
    """Interactive keyword selection."""
    print("\n📋 Select Keywords (for categorization)")
    print("-" * 60)

    keywords = []

    # Modality
    print("\n1. Modality (select one or more):")
    print("   1) CP-LiDAR")
    print("   2) CP-Camera")
    print("   3) CP-Fusion (LiDAR-Camera)")
    modality_choices = get_input("   Enter numbers separated by commas (e.g., 1,2): ", required=True)

    modality_map = {
        '1': 'CP-LiDAR',
        '2': 'CP-Camera',
        '3': 'CP-Fusion'
    }
    for choice in modality_choices.split(','):
        choice = choice.strip()
        if choice in modality_map:
            keywords.append(modality_map[choice])

    # Collaboration Type
    print("\n2. Collaboration Type (select one):")
    print("   1) CP-Early (raw data sharing)")
    print("   2) CP-Intermediate (feature sharing)")
    print("   3) CP-Late (result sharing)")
    print("   4) CP-Hybrid (multiple strategies)")
    collab_choice = get_input("   Enter number: ", required=True)

    collab_map = {
        '1': 'CP-Early',
        '2': 'CP-Intermediate',
        '3': 'CP-Late',
        '4': 'CP-Hybrid'
    }
    if collab_choice in collab_map:
        keywords.append(collab_map[collab_choice])

    # Perception Task
    print("\n3. Perception Task (select one or more):")
    print("   1) CP-Object Detection")
    print("   2) CP-Object Tracking")
    print("   3) CP-Semantic Segmentation")
    print("   4) CP-Motion Prediction")
    print("   5) CP-Lane Detection")
    print("   6) CP-Multi-task")
    task_choices = get_input("   Enter numbers separated by commas: ", required=True)

    task_map = {
        '1': 'CP-Object Detection',
        '2': 'CP-Object Tracking',
        '3': 'CP-Semantic Segmentation',
        '4': 'CP-Motion Prediction',
        '5': 'CP-Lane Detection',
        '6': 'CP-Multi-task'
    }
    for choice in task_choices.split(','):
        choice = choice.strip()
        if choice in task_map:
            keywords.append(task_map[choice])

    return keywords


def generate_bibtex_entry(entry_data, keywords):
    """Generate formatted BibTeX entry."""

    # Generate citation key
    first_author = entry_data['author'].split(' and ')[0].split(',')[0].strip()
    year = entry_data['year']
    title_words = entry_data['title'].split()[:2]
    title_part = ''.join(title_words)
    citation_key = f"{title_part}-{year}-{first_author.lower()}"

    # Determine entry type
    entry_type = entry_data['type']

    # Build BibTeX entry
    bibtex = f"@{entry_type}{{{citation_key},\n"
    bibtex += f"  title = {{{{{entry_data['title']}}}}},\n"

    if entry_type == 'inproceedings':
        bibtex += f"  booktitle = {{{{{entry_data['venue']}}}}},\n"
    else:
        bibtex += f"  journal = {{{{{entry_data['venue']}}}}},\n"

    bibtex += f"  author = {{{entry_data['author']}}},\n"
    bibtex += f"  year = {{{entry_data['year']}}},\n"

    if entry_data.get('doi'):
        bibtex += f"  doi = {{{entry_data['doi']}}},\n"

    if entry_data.get('arxiv'):
        bibtex += f"  eprint = {{{entry_data['arxiv']}}},\n"

    # Add keywords
    keywords_str = ', '.join(keywords)
    bibtex += f"  keywords = {{{keywords_str}}},\n"

    bibtex += "}\n"

    return bibtex, citation_key


def main():
    """Main interactive function."""
    print_header()

    print("This tool helps you add a new paper to the repository.")
    print("Please provide the following information:\n")

    # Collect basic information
    entry_data = {}

    # Entry type
    print("Entry Type:")
    print("  1) Conference Paper (inproceedings)")
    print("  2) Journal Article (article)")
    entry_type_choice = get_input("Select (1 or 2): ", required=True)
    entry_data['type'] = 'inproceedings' if entry_type_choice == '1' else 'article'

    # Title
    entry_data['title'] = get_input("\nTitle: ", required=True)

    # Authors (in BibTeX format)
    print("\nAuthors (format: LastName, FirstName and LastName, FirstName):")
    print("  Example: Smith, John and Doe, Jane")
    entry_data['author'] = get_input("Authors: ", required=True)

    # Year
    entry_data['year'] = get_input("\nYear: ", required=True)

    # Venue
    venue_label = "Conference Name" if entry_data['type'] == 'inproceedings' else "Journal Name"
    entry_data['venue'] = get_input(f"\n{venue_label}: ", required=True)

    # DOI (optional)
    entry_data['doi'] = get_input("\nDOI (optional, press Enter to skip): ", required=False)

    # arXiv (optional)
    entry_data['arxiv'] = get_input("arXiv ID (optional, press Enter to skip): ", required=False)

    # Select keywords
    keywords = select_keywords()

    # Generate BibTeX entry
    print("\n" + "=" * 60)
    print("Generated BibTeX Entry:")
    print("=" * 60)
    bibtex_entry, citation_key = generate_bibtex_entry(entry_data, keywords)
    print(bibtex_entry)

    # Confirm
    confirm = get_input("\nAdd this entry to collaborative-perception.bib? (y/n): ", required=True)

    if confirm.lower() in ['y', 'yes']:
        # Find BibTeX file
        bib_path = Path(__file__).parent.parent / "collaborative-perception.bib"

        if not bib_path.exists():
            print(f"\n⚠ Error: BibTeX file not found at {bib_path}")
            print("Please run this script from the tools directory.")
            sys.exit(1)

        # Append to BibTeX file
        with open(bib_path, 'a', encoding='utf-8') as f:
            f.write("\n" + bibtex_entry)

        print(f"\n✓ Successfully added {citation_key} to collaborative-perception.bib")

        # Suggest next steps
        print("\nNext steps:")
        print("  1. Run parser: python tools/data_extraction/bib_parser.py")
        print("  2. Generate README: python tools/data_extraction/readme_generator.py")
        print("  3. Commit changes: git add . && git commit -m 'Add paper: {}'".format(entry_data['title'][:50]))
    else:
        print("\n✗ Entry not added. You can copy the BibTeX entry above and add it manually.")

    print("\n" + "=" * 60)
    print("Done!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✗ Cancelled by user.")
        sys.exit(0)
