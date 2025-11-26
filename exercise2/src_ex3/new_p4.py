def candidate(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)
