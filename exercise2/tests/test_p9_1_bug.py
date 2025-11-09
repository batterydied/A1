import pytest
from src.p9_bug import candidate

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

def test_candidate(numbers, expected):
    assert candidate(numbers) == expected


def test_empty_list():
    assert candidate([]) == []


def test_none_input():
    with pytest.raises(TypeError):
        candidate(None)


def test_string_input():
    with pytest.raises(TypeError):
        candidate("123")


def test_float_input():
    with pytest.raises(TypeError):
        candidate(123.45)


def test_dict_input():
    with pytest.raises(TypeError):
        candidate({"a": 1, "b": 2})


def test_set_input():
    with pytest.raises(TypeError):
        candidate({1, 2, 3})


def test_bool_input():
    with pytest.raises(TypeError):
        candidate(True)
