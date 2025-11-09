from typing import List

def candidate(paren_string: str) -> list[int]:
    max_depth = 0
    current_depth = 0
    result = []

    for char in paren_string:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            if current_depth > max_depth:
                max_depth = current_depth
            current_depth -= 1

    return [max_depth]
