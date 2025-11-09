import pytest
from src.p9 import candidate

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [4, 4, 4, 4]),
    ([3, 2, 3, 100, 3], [3, 3, 3, 100, 100]),
    ([-1, 2, 3], [-1, 2, 3]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 1, 2, 2, 1], [1, 1, 2, 2, 2]),
    ([-5, -4, -3, -10], [-5, -4, -3, -3]),
    ([10], [10]),
    ([5, 10, 5, 10, 5, 10], [5, 10, 10, 10, 10, 10]),
])

def test_humaneval9(numbers, expected):
    assert candidate(numbers) == expected
