import pytest
from src.p1 import candidate

@pytest.mark.parametrize("paren_string, expected", [
    ('(()()) ((())) () ((())()())', ['(()())', '((()))', '()', '((())()())']),
    ('() (()) ((())) (((())))', ['()', '(())', '((()))', '(((())))']),
    ('(()(())((())))', ['(()(())((())))']),
    ('( ) (( )) (( )( ))', ['()', '(())', '(()())']),
    ('', []),
    ('()', ['()']),
])

def test_humaneval1(paren_string, expected):
    assert candidate(paren_string) == expected
