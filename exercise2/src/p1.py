from typing import List

def candidate(paren_string: str) -> list[str]:
    result = []
    temp = ''
    balance = 0
    for char in paren_string:
        if char == '(':
            balance += 1
            temp += char
        elif char == ')':
            balance -= 1
            temp += char
            if balance == 0:
                result.append(temp)
                temp = ''
    return result
