import pytest
from src.p8 import candidate

@pytest.mark.parametrize("numbers, expected", [
    ([], (0, 1)),
    ([1, 1, 1], (3, 1)),
    ([100, 0], (100, 0)),
    ([3, 5, 7], (15, 105)),
    ([10], (10, 10)),
    ([1, -1, 2, -2], (0, 4)),
    ([1, 2, 3, 4, 5], (15, 120)),
])

def test_humaneval8(numbers, expected):
    assert candidate(numbers) == expected
