CoT_templates = [
"""
Task:
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
def truncate_number(number: float) -> float:
    \"\"\" Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List

def below_zero(operations: List[int]) -> bool:
    \"\"\" You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    \"\"\" For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    \"\"\" Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    \"\"\"


Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    \"\"\" Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    \"\"\" Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    \"\"\" For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
""",

"""
Task:
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    \"\"\" From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    \"\"\"

Think step by step and then output only the solution (Do not leave any comments)

Make sure you change the name of the function to "candidate"
"""
]
