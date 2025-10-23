revised_SCoT_templates = ['''
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    \"\"\"

Follow these rules:
1. Think through the problem and design them step by step.
2. Keep all reasoning internal, do not output your thought process.
3. Use standard programming construct, no non-deterministic shortcuts.
4. Do not use any hardcoded solutions.
5. After completing your reasoning, output only the solution (Do not leave any comments)
6. Make sure the function is named as "candidate"
''']