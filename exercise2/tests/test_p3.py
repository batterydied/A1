import pytest
from src.p3 import candidate

@pytest.mark.parametrize("numbers, expected", [
    ([], False),
    ([1, 2, -3, 1, 2, -3], False),
    ([1, 2, -4, 5, 6], True),
    ([1, -1, 2, -2, 5, -5, 4, -4], False),
    ([1, -1, 2, -2, 5, -5, 4, -5], True),
    ([100, -50, -60], True),
    ([-1], True),
    ([0], False),
])

def test_humaneval3(numbers, expected):
    assert candidate(numbers) == expected
