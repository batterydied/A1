from huggingface_hub import InferenceClient
import os
import json

client = InferenceClient(
    provider="novita",
)

MODEL = 'meta-llama/Llama-3.1-8B-Instruct'
PROMPT = f'generate test cases for the following function: '

functions = {
    'p4': '''
    from typing import List

def candidate(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)
    ''',
    'p9': '''from typing import List

def candidate(numbers: List[int]) -> List[int]:
    result = []
    if numbers == []:
        return result
    max_so_far = float('-inf')
    for num in numbers:
        max_so_far = max(max_so_far, num)
        result.append(max_so_far)
    return result'''
}

test_examples = {
    'p4':'''
@pytest.mark.parametrize("numbers, expected, tolerance", [
    ([1.0, 2.0, 3.0], 2.0 / 3.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0], 1.0, 1e-6),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 6.0 / 5.0, 1e-6),
    ([1.0, 1.0, 1.0], 0.0, None),
    ([10.0, 0.0], 5.0, None),
    ([0.0, 0.0, 10.0], 40 / 9, 1e-6),
])
''',
    'p9': '''
    @pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([4, 3, 2, 1], [4, 4, 4, 4]),
    ([3, 2, 3, 100, 3], [3, 3, 3, 100, 100]),
    ([-1, 2, 3], [-1, 2, 3]),
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 1, 2, 2, 1], [1, 1, 2, 2, 2]),
    ([-5, -4, -3, -10], [-5, -4, -3, -3]),
    ([10], [10]),
    ([5, 10, 5, 10, 5, 10], [5, 10, 10, 10, 10, 10]),
])'''
}

def generate_test(p_num, it_num):

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": f'''
                    Given the following Python function:
                    {functions[p_num]}
                    Generate comprehensive pytest-style unit tests for this function.

                    Use the following format and style as a guide:
                    {test_examples[p_num]}

                    Return only valid Python code (no prose, no markdown, no comments).
                    The output must include at least one @pytest.mark.parametrize test function named test_candidate,
                    covering normal cases, edge cases, and invalid input cases.
                '''
            }
        ],
    )

    content = completion.choices[0].message.content

    dir_path = os.path.join("outputs")
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, f"{p_num}_{it_num}.json")

    data = [
        {'code': content}
    ]
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


generate_test('p9', '1')
