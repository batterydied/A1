import pytest
from src.p2 import candidate

@pytest.mark.parametrize("number, expected, tolerance", [
    (3.5, 0.5, None),
    (1.33, 0.33, 1e-6),
    (123.456, 0.456, 1e-6),
    (0.9999, 0.9999, 1e-6),
    (10.0, 0.0, None),
])

def test_humaneval2(number, expected, tolerance):
    result = candidate(number)
    if tolerance is not None:
        assert abs(result - expected) < tolerance
    else:
        assert result == expected
