from typing import List

def candidate(numbers, delimeter):
    result = []
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            result.append(num)
        if i > 0:
            result.append(delimeter)
    return result
