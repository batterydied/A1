from typing import List

def candidate(numbers: List[int]) -> List[int]:
    result = []
    if numbers == []:
        return result
    max_so_far = float('-inf')
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    return result
