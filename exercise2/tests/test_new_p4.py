import pytest
from src_ex3.new_p4 import candidate

@pytest.mark.parametrize("numbers, expected, tolerance", [
    ([1.0, 2.0, 3.0], 2.0 / 3.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0], 1.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 6.0 / 5.0, 1e-6),
    ([1.0, 1.0, 1.0], 0.0, None),
    ([10.0, 0.0], 5.0, None),
    ([0.0, 0.0, 10.0], 40 / 9, 1e-6),

    #Spec-guided tests (Assignment 3)

    ([1.0, 2.0], 0.5, 1e-6),
    ([3.0, 3.0, 3.0], 0.0, None),
    ([1.0, 2.0, 3.0], 2.0 / 3.0, 1e-6),
    ([5.0, 5.0, 5.0], 0.0, None),
    ([-1.0, 1.0], 1.0, None)
])
def test_p4_spec_guided(numbers, expected, tolerance):
    res = candidate(numbers)
    if tolerance is None:
        assert res == expected
    else:
        assert abs(res - expected) < tolerance
