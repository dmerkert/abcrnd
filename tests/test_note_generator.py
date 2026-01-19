#!/usr/bin/env python3
# Copyright (C) 2026 dmerkert
# Licensed under GPL-3.0 - see LICENSE file for details
"""
Unit tests for the Music Note Learning Generator.
Tests all functions and validates output format.
"""

import unittest
import sys
import os
from datetime import date
from unittest.mock import patch
from io import StringIO

# Add parent directory to path to import note_generator
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import note_generator


class TestGenerateRandomNotes(unittest.TestCase):
    """Tests for the generate_random_notes function."""

    def test_default_count(self):
        """Test that default count generates 32 notes."""
        notes = note_generator.generate_random_notes()
        self.assertEqual(len(notes), 32)

    def test_custom_count(self):
        """Test that custom count parameter works correctly."""
        for count in [8, 16, 64]:
            notes = note_generator.generate_random_notes(count)
            self.assertEqual(len(notes), count)

    def test_valid_note_range(self):
        """Test that all generated notes are in valid range (C4-C5)."""
        valid_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'c']
        notes = note_generator.generate_random_notes(100)
        for note in notes:
            self.assertIn(note, valid_notes)

    def test_randomness(self):
        """Test that function generates different sequences on multiple calls."""
        notes1 = note_generator.generate_random_notes(32)
        notes2 = note_generator.generate_random_notes(32)
        # With 32 notes from 8 choices, extremely unlikely to be identical
        self.assertNotEqual(notes1, notes2)

    def test_all_notes_can_be_generated(self):
        """Test that all valid notes can potentially be generated."""
        valid_notes = set(['C', 'D', 'E', 'F', 'G', 'A', 'B', 'c'])
        # Generate many notes to ensure we get all possibilities
        all_notes = note_generator.generate_random_notes(1000)
        generated_notes = set(all_notes)
        # We should see all valid notes in 1000 random selections
        self.assertEqual(generated_notes, valid_notes)


class TestFormatAbcNotation(unittest.TestCase):
    """Tests for the format_abc_notation function."""

    def test_header_format(self):
        """Test that ABC notation headers are correctly formatted."""
        notes = ['C', 'D', 'E', 'F'] * 8
        date_str = "2026-01-19"
        result = note_generator.format_abc_notation(notes, date_str)

        # Check for required header fields
        self.assertIn("X: 1", result)
        self.assertIn(f"T: {date_str} Notenübung", result)
        self.assertIn("M: 4/4", result)
        self.assertIn("L: 1/4", result)
        self.assertIn("K: C", result)

    def test_measure_structure(self):
        """Test that notes are grouped into measures with pipes."""
        notes = ['C', 'D', 'E', 'F'] * 8
        date_str = "2026-01-19"
        result = note_generator.format_abc_notation(notes, date_str)

        # Should have pipes separating measures
        self.assertIn('|', result)

        # Count measure separators (should be 9 pipes: 8 measures + 1 ending)
        pipe_count = result.count('|')
        self.assertGreaterEqual(pipe_count, 8)

    def test_32_notes_format(self):
        """Test formatting with exactly 32 notes (standard case)."""
        notes = ['A'] * 32
        date_str = "2026-01-19"
        result = note_generator.format_abc_notation(notes, date_str)

        # Count 'A's in the note lines (skip headers)
        lines = result.split('\n')
        note_lines = [line for line in lines if '|' in line]
        total_a = sum(line.count('A') for line in note_lines)
        self.assertEqual(total_a, 32)

    def test_two_line_output(self):
        """Test that output has two lines of measures."""
        notes = ['C'] * 32
        date_str = "2026-01-19"
        result = note_generator.format_abc_notation(notes, date_str)

        # Count lines with pipe symbols (measure lines)
        lines = result.split('\n')
        measure_lines = [line for line in lines if '|' in line and not line.startswith(('X:', 'T:', 'M:', 'L:', 'K:'))]
        self.assertEqual(len(measure_lines), 2)


class TestGenerateMarkdownOutput(unittest.TestCase):
    """Tests for the generate_markdown_output function."""

    def test_markdown_structure(self):
        """Test that output has proper markdown structure."""
        with patch('note_generator.date') as mock_date:
            mock_date.today.return_value = date(2026, 1, 19)
            mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

            output = note_generator.generate_markdown_output()

            # Check for H1 heading
            self.assertTrue(output.startswith('#'))
            self.assertIn('2026-01-19 Notenübung', output)

            # Check for ABC code fence
            self.assertIn('```abc', output)
            self.assertIn('```\n', output)

    def test_date_format(self):
        """Test that date is formatted as YYYY-MM-DD."""
        with patch('note_generator.date') as mock_date:
            mock_date.today.return_value = date(2026, 1, 19)
            mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

            output = note_generator.generate_markdown_output()
            self.assertIn('2026-01-19', output)

    def test_abc_notation_included(self):
        """Test that ABC notation is included in markdown."""
        output = note_generator.generate_markdown_output()

        # Check for ABC headers
        self.assertIn('X: 1', output)
        self.assertIn('M: 4/4', output)
        self.assertIn('K: C', output)

    def test_output_completeness(self):
        """Test that output includes all required sections."""
        output = note_generator.generate_markdown_output()

        # Title
        self.assertIn('# ', output)
        self.assertIn('Notenübung', output)

        # ABC code block
        self.assertIn('```abc', output)

        # ABC headers
        self.assertIn('X: 1', output)
        self.assertIn('T: ', output)
        self.assertIn('M: 4/4', output)
        self.assertIn('L: 1/4', output)
        self.assertIn('K: C', output)

        # Measure separators
        self.assertIn('|', output)


class TestMainFunction(unittest.TestCase):
    """Tests for the main function (CLI interface)."""

    def test_main_output_to_stdout(self):
        """Test that main function outputs to stdout."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            note_generator.main()
            output = fake_out.getvalue()

            # Should produce some output
            self.assertGreater(len(output), 0)

            # Should contain markdown structure
            self.assertIn('#', output)
            self.assertIn('```abc', output)

    def test_main_no_trailing_newline(self):
        """Test that main output ends without extra newline."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            note_generator.main()
            output = fake_out.getvalue()

            # Output should not end with double newline
            self.assertFalse(output.endswith('\n\n'))


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow."""

    def test_full_pipeline(self):
        """Test that the full pipeline produces valid output."""
        output = note_generator.generate_markdown_output()

        # Parse the output
        lines = output.split('\n')

        # Check heading
        self.assertTrue(lines[0].startswith('#'))

        # Find ABC block
        abc_start = None
        abc_end = None
        for i, line in enumerate(lines):
            if line.strip() == '```abc':
                abc_start = i
            elif abc_start is not None and line.strip() == '```':
                abc_end = i
                break

        self.assertIsNotNone(abc_start)
        self.assertIsNotNone(abc_end)

        # Extract ABC content
        abc_content = '\n'.join(lines[abc_start+1:abc_end])

        # Validate ABC structure
        self.assertIn('X: 1', abc_content)
        self.assertIn('T: ', abc_content)
        self.assertIn('M: 4/4', abc_content)
        self.assertIn('L: 1/4', abc_content)
        self.assertIn('K: C', abc_content)

        # Count notes in measure lines
        measure_lines = [line for line in abc_content.split('\n') if '|' in line]
        self.assertEqual(len(measure_lines), 2)

        # Count total notes (exclude pipes and spaces)
        all_notes = ''.join(measure_lines).replace('|', '').replace(' ', '')
        self.assertEqual(len(all_notes), 32)

    def test_reproducible_with_seed(self):
        """Test that output is reproducible when random seed is set."""
        import random

        random.seed(42)
        output1 = note_generator.generate_markdown_output()

        random.seed(42)
        output2 = note_generator.generate_markdown_output()

        # ABC content should be identical (excluding date which uses real time)
        self.assertEqual(output1, output2)


if __name__ == '__main__':
    unittest.main()
