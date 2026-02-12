#!/usr/bin/env python3
# Copyright (C) 2026 dmerkert
# Licensed under GPL-3.0 - see LICENSE file for details
"""
Music Note Learning Generator
Generates random music note exercises for piano beginners learning treble clef.
Output is in Obsidian-compatible markdown format with ABC notation.
"""

import random
import argparse
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


def generate_scale_reference():
    """
    Generate a C major scale reference in ABC notation.

    Returns:
        String containing ABC notation for the C major scale with note labels
    """
    abc_lines = [
        "X: 1",
        "T: Tonleiter",
        "M: 4/4",
        "L: 1/4",
        "K: C",
        '"C"C"D"D"E"E"F"F|"G"G"A"A"H"B"C"c||'
    ]

    return '\n'.join(abc_lines)


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

    # Format notes into measures (4 notes per measure)
    measures = []
    for i in range(0, len(notes), 4):
        measure = ''.join(notes[i:i+4])
        measures.append(measure)

    # Group measures into lines (4 measures per line)
    for i in range(0, len(measures), 4):
        line_measures = measures[i:i+4]
        line = '|'.join(line_measures)
        if i + 4 >= len(measures):
            # Last line gets a double bar
            abc_lines.append(line + "||")
        else:
            # Other lines get a single bar
            abc_lines.append(line + "|")

    return '\n'.join(abc_lines)


def generate_markdown_output(include_scale_reference=False):
    """
    Generate complete markdown output with date title and ABC notation.

    Args:
        include_scale_reference: If True, includes a C major scale reference before the exercise

    Returns:
        String containing complete markdown document
    """
    # Get current date in YYYY-MM-DD format
    today = date.today()
    date_str = today.strftime("%Y-%m-%d")

    # Build markdown document
    markdown = f"# {date_str} Notenübung\n\n"

    # Add scale reference if requested
    if include_scale_reference:
        markdown += "```abc\n"
        markdown += generate_scale_reference() + "\n"
        markdown += "```\n\n"

    # Generate random notes
    notes = generate_random_notes(32)

    # Format ABC notation
    abc_content = format_abc_notation(notes, date_str)

    markdown += "```abc\n"
    markdown += abc_content + "\n"
    markdown += "```\n"

    return markdown


def main(argv=None):
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Generate random music note exercises for piano beginners learning treble clef."
    )
    parser.add_argument(
        '-s', '--scale-reference',
        action='store_true',
        help='Include a C major scale reference before the exercise'
    )

    args = parser.parse_args(argv)

    output = generate_markdown_output(include_scale_reference=args.scale_reference)
    print(output, end='')


if __name__ == "__main__":
    main()
