# Project Requirements Document

## 1. Project Overview
- **Project Name**: Music Note Learning Generator
- **Vision**: A simple command-line tool to generate random music note exercises for piano beginners learning to read notes in treble clef
- **Target Users**: Parent (Dennis) generating exercises for his son to practice note reading
- **Context**: Dennis's son is learning piano and needs to practice reading and identifying notes in treble clef (violin key), specifically recognizing note positions on the staff and finding them on the keyboard. The tool generates Obsidian-compatible markdown files with ABC notation that can be used for offline practice sessions.

## 2. User Stories & Use Cases

### Primary User Stories
- As a parent, I want to generate random note exercises so that my son can practice reading treble clef notes
- As a parent, I want the output in Obsidian-compatible markdown format so that I can use it with my existing note-taking system
- As a parent, I want a simple command-line tool so that I can quickly generate new exercises without configuration overhead

### Detailed Use Cases

**Use Case 1: Generate Practice Exercise**
- Primary flow:
  1. User executes `python note_generator.py` from command line
  2. Script generates 32 random notes in the range C4-C5 (middle C to C one octave above)
  3. Script outputs markdown to stdout containing current date and ABC notation
  4. User redirects output to file or copies it into Obsidian vault
  5. User practices with child using the generated notes displayed in Obsidian

- Alternative flows:
  - User pipes output directly to a file: `python note_generator.py > exercise.md`
  - User copies output from terminal and pastes into existing Obsidian note

- Error scenarios:
  - Python not installed or wrong version: Script should fail with clear Python version error
  - Invalid Python environment: Standard Python error messages apply

- Edge cases:
  - Script run on different date should generate new date in title
  - Multiple runs on same day generate different random notes each time

## 3. Functional Requirements

### Note Generation
- **REQ-1.1**: Generate exactly 32 random notes
- **REQ-1.2**: Each note must be within the range C4 to C5 (inclusive)
- **REQ-1.3**: Only use white keys (C, D, E, F, G, A, B) - no sharps or flats
- **REQ-1.4**: All notes are quarter notes (crotchets)
- **REQ-1.5**: Random distribution should be truly random (no seed, no reproducibility)

### Musical Formatting
- **REQ-2.1**: Organize notes in 4/4 time signature
- **REQ-2.2**: Create 8 complete measures (bars) total
- **REQ-2.3**: Each measure contains exactly 4 quarter notes
- **REQ-2.4**: Format output with 4 measures per line (2 lines total)

### ABC Notation Output
- **REQ-3.1**: Generate valid ABC notation compatible with Obsidian's "ABC Music Notation" plugin
- **REQ-3.2**: Include proper ABC header fields:
  - X: reference number
  - T: title (date + "Notenübung")
  - M: meter (4/4)
  - L: default note length (1/4)
  - K: key signature (C major)
- **REQ-3.3**: Format ABC code with proper measure separators (|)
- **REQ-3.4**: Include line breaks after every 4 measures for readability

### Markdown Output
- **REQ-4.1**: Output complete markdown document to stdout
- **REQ-4.2**: Include title as H1 heading: `# yyyy-mm-dd Notenübung`
- **REQ-4.3**: Use current date in format YYYY-MM-DD (e.g., 2026-01-18)
- **REQ-4.4**: Embed ABC notation in proper code fence for Obsidian plugin (` ```abc `)

### Command-Line Interface
- **REQ-5.1**: Script named `note_generator.py`
- **REQ-5.2**: Execute without any command-line parameters or arguments
- **REQ-5.3**: Simple invocation: `python note_generator.py`
- **REQ-5.4**: No interactive prompts or user input required
- **REQ-5.5**: Output sent to stdout (can be piped or redirected)

## 4. Acceptance Criteria

### Note Generation is complete when:
- Running script 10 times produces 10 different random sequences of notes
- All generated notes fall within C4-C5 range (no notes outside this octave)
- No sharps (#) or flats (b) appear in any generated output
- Exactly 32 notes are generated in every run
- All notes have quarter note duration (no eighth notes, half notes, or whole notes)

### Musical Formatting is complete when:
- ABC output contains exactly 8 measures
- Each measure contains exactly 4 quarter notes (no more, no less)
- Measures are separated by | symbols
- Visual formatting shows 4 measures on first line, 4 measures on second line
- Time signature is correctly set to 4/4 in ABC header

### ABC Notation Output is complete when:
- Generated ABC code renders correctly in Obsidian using ABC Music Notation plugin
- ABC header includes all required fields (X, T, M, L, K)
- ABC code follows standard ABC notation syntax
- Notes are encoded using correct ABC pitch notation (C, D, E, F, G, A, B, c for respective octaves)
- Code can be copied directly into Obsidian without modification

### Markdown Output is complete when:
- Title shows current date in YYYY-MM-DD format
- Title includes " Notenübung" text after date
- ABC code is properly fenced in ```abc code block
- Complete markdown renders correctly when pasted into Obsidian
- Output can be successfully piped to file: `python note_generator.py > test.md`

### Command-Line Interface is complete when:
- Script runs with simple `python note_generator.py` command
- Script runs successfully with Python 3.8+
- Script exits with code 0 on successful execution
- No parameters are required or accepted
- No interactive input is requested from user

## 5. Non-Functional Requirements

### Usability
- Script should execute in under 1 second
- Output should be immediately visible in terminal for copy-paste
- No configuration files or setup required

### Maintainability
- Code should be simple and readable (single file)
- Standard Python code style (PEP 8)
- Basic comments explaining ABC notation structure

### Portability
- Must work on Python 3.x (generic compatibility, no specific minor version required)
- Must use only Python standard library (no external dependencies)
- Should work on any operating system that supports Python 3

## 6. Technical Constraints

- Must use only Python standard library (no pip packages)
- Must output to stdout (not directly to files)
- Must work with Python 3.x without version-specific features
- Must generate ABC notation compatible with Obsidian's "ABC Music Notation" plugin

## 7. Dependencies

### External Dependencies
- Python 3.x runtime environment
- Obsidian application with "ABC Music Notation" plugin (for viewing, not for script execution)

### No Library Dependencies
- Script uses only Python standard library modules (random, datetime, sys)

## 8. Prioritization

### Must-Have (MVP)
- Generate 32 random notes in C4-C5 range (white keys only)
- Output markdown with date title
- Format as 4/4 time with quarter notes
- Valid ABC notation in code fence
- 4 measures per line, 8 measures total
- Simple command-line execution without parameters

### Should-Have
- N/A (all features are MVP)

### Nice-to-Have
- N/A (intentionally keeping scope minimal)

## 9. Out of Scope

**Explicitly NOT included:**
- Bass clef (F clef) support
- Black keys / accidentals (sharps and flats)
- Variable note ranges or configurable parameters
- Different time signatures (only 4/4)
- Variable note durations (only quarter notes)
- Rests or pauses
- Command-line arguments or configuration
- Reproducibility / random seed control
- Audio playback or MIDI generation
- Interactive features (feedback on correct/incorrect answers)
- Progress tracking or statistics
- Saving to files directly (use stdout redirection instead)
- Multiple exercises or batch generation
- GUI or web interface
- Exercise difficulty levels
- Support for other notation formats (MusicXML, MIDI files, etc.)
- Integration with external music learning platforms
- Automated printing or PDF generation
