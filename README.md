# Interstice

`interstice` is a Python package that simulates a game involving soldiers and demons on a 10x10 grid. This package processes a 100-character string input to initialize the game state and determines the number of turns required for either soldiers or demons to win.

## Installation

Install the package using pip (replace the version number as needed):

```bash
pip install interstice
```

## Usage

### Importing and Running the Game

The `interstice` package provides a single callable function, `interstice`, which takes a 100-character string as input and returns the number of turns the game lasted.

### Example

```python
from interstice import interstice

# Create a 100-character string with 'x', '*', and 'S'.
random_string = "S" * 50 + "*" * 30 + "x" * 20

# Run the game simulation
turns = interstice(random_string)
print(f"The game ended in {turns} turns.")
```

### Input Validation
The input string must:
- Be exactly 100 characters long.
- Contain only the characters `'x'`, `'*'`, or `'S'`.

If the input is invalid, the function raises a `ValueError`.

### Example Invalid Input

```python
from interstice import interstice

# Invalid input
invalid_string = "S" * 101  # More than 100 characters

try:
    turns = interstice(invalid_string)
except ValueError as e:
    print(f"Error: {e}")
```

## License
This project is licensed under the MIT License.
