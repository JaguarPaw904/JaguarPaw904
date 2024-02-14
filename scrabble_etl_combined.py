# scrabble_etl.py

# Define the legacy Scrabble scores
legacy_scores = {
    "A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
    "D": 2, "G": 2,
    "B": 3, "C": 3, "M": 3, "P": 3,
    "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
    "K": 5,
    "J": 8, "X": 8,
    "Q": 10, "Z": 10
}

def transform_legacy_scores(legacy_scores):
    """
    Transforms the legacy Scrabble scores to the new format.

    Args:
        legacy_scores (dict): Dictionary mapping letters to their scores.

    Returns:
        dict: Dictionary mapping letters to their scores in the new format.
    """
    new_scores = {}
    for letter, score in legacy_scores.items():
        new_scores[letter.lower()] = score
    return new_scores

# If you want to test the function independently
# transformed_scores = transform_legacy_scores(legacy_scores)
# print(transformed_scores)


# scrabble_etl_test.py

import pytest
from scrabble_etl import transform_legacy_scores

# Define test cases
@pytest.mark.parametrize("legacy_scores, expected_result", [
    (
        {"A": 1, "E": 1, "I": 1, "O": 1, "U": 1, "L": 1, "N": 1, "R": 1, "S": 1, "T": 1,
         "D": 2, "G": 2,
         "B": 3, "C": 3, "M": 3, "P": 3,
         "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
         "K": 5,
         "J": 8, "X": 8,
         "Q": 10, "Z": 10},
        {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
         "d": 2, "g": 2,
         "b": 3, "c": 3, "m": 3, "p": 3,
         "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
         "k": 5,
         "j": 8, "x": 8,
         "q": 10, "z": 10}
    ),
    # Add more test cases if needed
])
def test_transform_legacy_scores(legacy_scores, expected_result):
    # Call the function under test
    result = transform_legacy_scores(legacy_scores)
    
    # Check if the result matches the expected output
    assert result == expected_result

if __name__ == "__main__":
    pytest.main()
