import pytest
from src_ex3.old_p4 import candidate

@pytest.mark.parametrize("numbers, expected, tolerance", [
    ([1.0, 2.0, 3.0], 2.0 / 3.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0], 1.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 6.0 / 5.0, 1e-6),
    ([1.0, 1.0, 1.0], 0.0, None),
    ([10.0, 0.0], 5.0, None),
    ([0.0, 0.0, 10.0], 40 / 9, 1e-6),
])

def test_humaneval4(numbers, expected, tolerance):
    result = candidate(numbers)
    if tolerance is not None:
        assert abs(result - expected) < tolerance
    else:
        assert result == expected
