from typing import List

def candidate(numbers: List[float], threshold: float) -> bool:
    numbers.sort()
    for i in range(len(numbers) - 1):
        if abs(numbers[i+1] - numbers[i]) <= threshold:
            return True
    return False
