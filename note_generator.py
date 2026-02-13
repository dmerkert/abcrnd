#!/usr/bin/env python3
# Copyright (C) 2026 dmerkert
# Licensed under GPL-3.0 - see LICENSE file for details
"""
Music Note Learning Generator
Generates random music note exercises for piano beginners learning treble clef.
Output is in Obsidian-compatible markdown format with ABC notation.
"""

import argparse
import random
from datetime import date


def generate_random_notes(count=32):
    """
    Generate random notes in the range C4-C5 (white keys only).

    Args:
        count: Number of notes to generate (default: 32)

    Returns:
        List of note strings in ABC notation
    """
    # ABC notation for white keys from C4 to C5
    # C, D, E, F, G, A, B are in the middle octave (C4-B4)
    # c is one octave higher (C5)
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'c']

    return [random.choice(notes) for _ in range(count)]


def format_abc_notation(notes, date_str):
    """
    Format notes as ABC notation with proper headers and measure structure.

    Args:
        notes: List of note strings
        date_str: Date string for the title

    Returns:
        String containing complete ABC notation
    """
    title = f"{date_str} Notenübung"

    # ABC header
    abc_lines = [
        "X: 1",
        f"T: {title}",
        "M: 4/4",
        "L: 1/4",
        "K: C"
    ]

    # Format notes into measures (4 notes per measure, 4 measures per line)
    measures = []
    for i in range(0, len(notes), 4):
        measure = ''.join(notes[i:i+4])
        measures.append(measure)

    # Create two lines with 4 measures each
    line1 = '|'.join(measures[0:4]) + '|'
    line2 = '|'.join(measures[4:8]) + '||'

    abc_lines.append(line1)
    abc_lines.append(line2)

    return '\n'.join(abc_lines)


def generate_reference_scale_abc():
    """Generate the reference C-c scale ABC block with note names."""
    return '\n'.join([
        "X: 1",
        "T: Tonleiter",
        "M: 4/4",
        "L: 1/4",
        "K: C",
        '"C"C"D"D"E"E"F"F"G"G"A"A"H"B"C"c',
    ])


def generate_markdown_output(include_reference_scale=False):
    """
    Generate complete markdown output with date title and ABC notation.

    Args:
        include_reference_scale: Whether to prepend a C-c reference scale block

    Returns:
        String containing complete markdown document
    """
    # Get current date in YYYY-MM-DD format
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")

    # Generate random notes
    notes = generate_random_notes(32)

    # Format ABC notation
    abc_content = format_abc_notation(notes, date_str)

    # Build markdown document
    markdown = ""

    if include_reference_scale:
        markdown += "# Tonleiter Referenz\n\n"
        markdown += "```abc\n"
        markdown += generate_reference_scale_abc() + "\n"
        markdown += "```\n\n"

    markdown += f"# {date_str} Notenübung\n\n"
    markdown += "```abc\n"
    markdown += abc_content + "\n"
    markdown += "```\n"

    return markdown


def parse_args(argv=None):
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Generate random ABC note exercises for piano beginners."
    )
    parser.add_argument(
        "--include-scale",
        action="store_true",
        help="Add a C-c scale reference block before the random exercise.",
    )
    return parser.parse_args(argv if argv is not None else [])


def main(argv=None):
    """Main entry point for the script."""
    args = parse_args(argv)
    output = generate_markdown_output(include_reference_scale=args.include_scale)
    print(output, end='')


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
