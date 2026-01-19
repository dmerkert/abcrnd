# Music Note Learning Generator

![Tests](https://github.com/dmerkert/abcrnd/workflows/Run%20Tests/badge.svg)
![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

A simple command-line tool that generates random music note exercises for piano beginners learning to read treble clef notation. Perfect for creating daily practice exercises in Obsidian-compatible markdown format with ABC notation.

## Features

- Generates 32 random notes in the range C4-C5 (middle C to C one octave above)
- Uses only white keys - perfect for beginners (C, D, E, F, G, A, B)
- Outputs in Obsidian-compatible markdown with ABC notation
- Creates properly formatted sheet music with 4/4 time signature
- Zero configuration - just run and get instant practice exercises
- No external dependencies - uses only Python standard library

## Requirements

- Python 3.8 or higher
- No external packages required

## Installation

Simply clone this repository:

```bash
git clone https://github.com/dmerkert/abcrnd.git
cd abcrnd
```

## Usage

Run the script directly to generate a new exercise:

```bash
python note_generator.py
```

Save the output to a file:

```bash
python note_generator.py > exercise.md
```

Or copy the terminal output directly into your Obsidian vault for instant practice.

## Example Output

```markdown
# 2026-01-19 Notenübung

\```abc
X: 1
T: 2026-01-19 Notenübung
M: 4/4
L: 1/4
K: C
CDEF|GABC|DEFG|ABCD|
EFGA|BCDE|FGAB|CDEF|
\```
```

When viewed in Obsidian with the [ABC Music Notation](https://github.com/abcjs-music/obsidian-plugin-abcjs) plugin, this renders as proper sheet music with a treble clef staff.

## How It Works

The generator creates exercises following these principles:

1. **Random Note Generation**: Each run generates 32 random quarter notes
2. **Beginner-Friendly Range**: Only uses C4-C5 (white keys only - no sharps or flats)
3. **Musical Structure**: Organizes notes into 8 measures of 4/4 time (4 notes per measure)
4. **Visual Layout**: Displays 4 measures per line for easy reading
5. **Date Stamping**: Each exercise is titled with the current date

## File Structure

```
.
├── note_generator.py          # Main script
├── tests/
│   ├── test_note_generator.py # Comprehensive test suite
│   └── __init__.py
├── .github/
│   └── workflows/
│       └── test.yml           # CI/CD pipeline
├── DESIGN.md                  # Design and requirements document
├── LICENSE                    # GPL-3.0 license
└── README.md                  # This file
```

## Running Tests

The project includes a comprehensive test suite:

```bash
python -m pytest tests/
```

Or using unittest:

```bash
python -m unittest discover tests
```

Tests cover:
- Note generation and randomness
- ABC notation formatting
- Markdown output structure
- Integration testing of the complete pipeline

## Use Case

This tool was created to help a parent generate daily practice exercises for their child learning piano. The exercises focus on:

- **Note Recognition**: Identifying notes on the treble clef staff
- **Keyboard Mapping**: Finding the corresponding keys on the piano
- **Reading Practice**: Building familiarity with note positions

Each practice session gets a unique, randomized exercise to prevent memorization and encourage genuine note-reading skills.

## Technical Details

### ABC Notation

The tool generates valid ABC notation with these specifications:
- **Reference Number (X)**: Always 1
- **Title (T)**: Current date + "Notenübung" (German for "note exercise")
- **Meter (M)**: 4/4 time signature
- **Default Length (L)**: Quarter notes (1/4)
- **Key (K)**: C major (no sharps or flats)

### Note Encoding

ABC notation pitch encoding used:
- `C, D, E, F, G, A, B` = C4-B4 (middle C through B)
- `c` = C5 (C one octave above middle C)

## CI/CD

This project uses GitHub Actions to automatically run tests on every pull request, ensuring code quality and preventing regressions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for piano students learning treble clef notation
- Compatible with [Obsidian](https://obsidian.md/) and the [ABC Music Notation plugin](https://github.com/abcjs-music/obsidian-plugin-abcjs)
- Uses the [ABC notation standard](https://abcnotation.com/) for music representation

---

**Happy practicing!**
