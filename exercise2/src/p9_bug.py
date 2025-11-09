from typing import List

def candidate(numbers: List[int]) -> List[int]:
    result = []
    if numbers == []:
        return result
    max_so_far = 0
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    return result
