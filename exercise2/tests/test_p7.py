import pytest
from src.p7 import candidate 

@pytest.mark.parametrize("strings, substring, expected", [
    ([], 'john', []),
    (['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx', ['xxx', 'xxxAAA', 'xxx']),
    (['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx', ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']),
    (['grunt', 'trumpet', 'prune', 'gruesome'], 'run', ['grunt', 'prune']),
    (['apple', 'banana', 'grape'], 'a', ['apple', 'banana', 'grape']),
    (['apple', 'banana', 'grape'], 'z', []),
    (['', ' '], '', ['', ' ']),
])

def test_humaneval7(strings, substring, expected):
    assert candidate(strings, substring) == expected
