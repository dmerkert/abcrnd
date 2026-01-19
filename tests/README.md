# Tests for Music Note Learning Generator

This directory contains comprehensive unit and integration tests for the `note_generator.py` script.

## Test Coverage

The test suite includes 17 tests organized into 6 test classes:

### 1. TestGenerateRandomNotes
Tests for the `generate_random_notes()` function:
- Default count (32 notes)
- Custom count parameter
- Valid note range (C4-C5)
- Randomness verification
- All notes can be generated

### 2. TestFormatAbcNotation
Tests for the `format_abc_notation()` function:
- Header format (X, T, M, L, K)
- Measure structure with pipes
- 32 notes formatting
- Two-line output structure

### 3. TestGenerateMarkdownOutput
Tests for the `generate_markdown_output()` function:
- Markdown structure (H1 heading)
- Date format (YYYY-MM-DD)
- ABC notation inclusion
- Output completeness

### 4. TestMainFunction
Tests for the `main()` CLI function:
- Output to stdout
- No trailing newline

### 5. TestIntegration
End-to-end integration tests:
- Full pipeline validation
- Reproducibility with random seed

## Running the Tests

### Using unittest (Python standard library)
```bash
# Run all tests with verbose output
python3 -m unittest tests.test_note_generator -v

# Run from the tests directory
cd tests
python3 -m unittest test_note_generator -v

# Run a specific test class
python3 -m unittest tests.test_note_generator.TestGenerateRandomNotes -v

# Run a specific test method
python3 -m unittest tests.test_note_generator.TestGenerateRandomNotes.test_default_count -v
```

### Using pytest (if installed)
```bash
# Run all tests with verbose output
pytest tests/test_note_generator.py -v

# Run with coverage report
pytest tests/test_note_generator.py --cov=note_generator --cov-report=term-missing
```

## Test Results

All tests pass successfully:
```
Ran 17 tests in 0.003s

OK
```

## Dependencies

The tests use only Python standard library modules:
- `unittest` - Testing framework
- `unittest.mock` - Mocking for isolated testing
- `io.StringIO` - Capturing stdout for testing
- `sys`, `os` - Path manipulation
- `datetime.date` - Date mocking

No external dependencies required!

## Adding New Tests

When adding new functionality to `note_generator.py`, follow these guidelines:

1. **Unit Tests**: Test individual functions in isolation
2. **Integration Tests**: Test the complete workflow
3. **Edge Cases**: Test boundary conditions and error cases
4. **Documentation**: Add docstrings explaining what each test validates

Example test structure:
```python
def test_new_feature(self):
    """Test description here."""
    # Arrange
    input_data = ...

    # Act
    result = function_to_test(input_data)

    # Assert
    self.assertEqual(result, expected_value)
```
