import pytest
from src.p5 import candidate

@pytest.mark.parametrize("numbers, value, expected", [
    ([], 7, []),
    ([5, 6, 3, 2], 8, [5, 8, 6, 8, 3, 8, 2]),
    ([2, 2, 2], 2, [2, 2, 2, 2, 2]),
    ([1], 9, [1]),
    ([1, 2], 0, [1, 0, 2]),
    (list(range(5)), -1, [0, -1, 1, -1, 2, -1, 3, -1, 4]),
])

def test_humaneval5(numbers, value, expected):
    assert candidate(numbers, value) == expected
