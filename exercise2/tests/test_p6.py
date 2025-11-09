import pytest
from src.p6 import candidate   # adjust filename as needed

@pytest.mark.parametrize("paren_string, expected", [
    ('(()()) ((())) () ((())()())', [2, 3, 1, 3]),
    ('() (()) ((())) (((())))', [1, 2, 3, 4]),
    ('(()(())((())))', [4]),
    ('', []),
    ('()', [1]),
    ('(((()))) (()())', [4, 2]),
])
def test_humaneval6(paren_string, expected):
    assert candidate(paren_string) == expected
