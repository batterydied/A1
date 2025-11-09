from src.p4 import candidate
import pytest

@pytest.mark.parametrize("numbers, expected, tolerance", [
    ([1.0, 2.0, 3.0], 2.0 / 3.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0], 1.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 6.0 / 5.0, 1e-6),
    ([1.0, 1.0, 1.0], 0.0, None),
    ([10.0, 0.0], 5.0, None),
    ([0.0, 0.0, 10.0], 40 / 9, 1e-6),
    ([], ValueError, None),
    ([1.0, 'a'], ValueError, None),
])
def test_candidate(numbers, expected, tolerance):
    try:
        result = candidate(numbers)
        # only reached for non-error cases
        if tolerance is None:
            assert result == expected
        else:
            assert abs(result - expected) <= tolerance
    except Exception as e:
        # only reached for error cases
        assert isinstance(e, expected), f"Expected {expected}, but got {type(e)}"