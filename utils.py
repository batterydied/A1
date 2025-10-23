import os
import traceback
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from prompts.CoT import CoT_templates
from prompts.SCoT import SCoT_templates
from prompts.revised_CoT_deepseek import revised_CoT_templates
from prompts.revised_SCoT_llama import revised_SCoT_templates
from prompts.innovated import innovated_templates
import json
import re

load_dotenv()
client = InferenceClient(
    provider="novita",
)

model_mapping = {
    'llama': 'meta-llama/Llama-3.1-8B-Instruct',
    'deepseek': 'deepseek-ai/DeepSeek-R1'
}

def generate_code(model, strategy, ques_num):
    MODEL = model_mapping[model]

    match strategy:
        case 'CoT':
            TEMPLATE = CoT_templates
        case 'SCoT':
            TEMPLATE = SCoT_templates
        case 'revised_CoT':
            TEMPLATE = revised_CoT_templates
        case 'revised_SCoT':
            TEMPLATE = revised_SCoT_templates
        case _:
            TEMPLATE = innovated_templates

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": TEMPLATE[ques_num]
            }
        ],
    )
    return completion.choices[0].message.content

def extract_code_block(text: str) -> str:
    """
    Extracts only the Python code portion from DeepSeek output.
    Removes reasoning or <think> sections.
    """
    # Remove <think>...</think> if they exist
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

    # Find the first occurrence of 'def candidate'
    match = re.search(r"def\s+candidate\s*\(.*", cleaned, flags=re.DOTALL)
    if match:
        # Return everything from 'def candidate' onward
        return cleaned[match.start():].strip()
    
    # If no 'def' found, return the cleaned text
    return cleaned.strip()

def save_output(model, strategy, ques_num, content, is_revised=False):
    dir_path = os.path.join("outputs", model, strategy)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, f"{'revised_' + 'p' + str(ques_num) if is_revised else 'p' + str(ques_num)}.json")

    data = [
        {'code': content}
    ]
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def generate_outputs():
    for i in range(10):
        deepseek_CoT = extract_code_block(generate_code('deepseek', 'CoT', ques_num=i))
        deepseek_SCoT = extract_code_block(generate_code('deepseek', 'SCoT', ques_num=i))
        llama_CoT = generate_code('llama', 'CoT', ques_num=i)
        llama_SCoT = generate_code('llama', 'SCoT', ques_num=i)

        save_output('deepseek', 'CoT', i, deepseek_CoT)
        save_output('deepseek', 'SCoT', i, deepseek_SCoT)
        save_output('llama', 'CoT', i, llama_CoT)
        save_output('llama', 'SCoT', i, llama_SCoT)

def generate_innovated_outputs():
    for i in range(10):
        deepseek_innovated = extract_code_block(generate_code('deepseek', 'innovated', ques_num=i))
        llama_innovated = extract_code_block(generate_code('llama', 'innovated', ques_num=i))

        save_output('deepseek', 'innovated', i, deepseek_innovated)
        save_output('llama', 'innovated', i, llama_innovated)

def generate_revised_outputs():
    deepseek_CoT = extract_code_block(generate_code('deepseek', 'revised_CoT', ques_num=0))
    llama_SCoT = generate_code('llama', 'revised_SCoT', ques_num=0)

    save_output('deepseek', 'CoT', 8, deepseek_CoT, True)
    save_output('llama', 'SCoT', 1, llama_SCoT, True)

tests = {
    "humanEval_0": [
        (([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3), True),
        (([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05), False),
        (([1.0, 2.0, 5.9, 4.0, 5.0], 0.95), True),
        (([1.0, 2.0, 5.9, 4.0, 5.0], 0.8), False),
        (([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1), True),
        (([1.1, 2.2, 3.1, 4.1, 5.1], 1.0), True),
        (([1.1, 2.2, 3.1, 4.1, 5.1], 0.5), False),
        (([], 0), False),
        (([1.0], 1.0), False),
        (([1.0, 1.000001], 0.00001), True),
        (([1.0, 5.0, 10.0, 15.0], 5.0), True),
        (([float('inf'), 1.0], float('inf')), False),
        (([float('-inf'), 1.0], float('inf')), False),
        (([float('-inf'), float('inf')], 1e100), False),
    ],
    "humanEval_1": [
        (('(()()) ((())) () ((())()())',), ['(()())', '((()))', '()', '((())()())']),
        (('() (()) ((())) (((())))',), ['()', '(())', '((()))', '(((())))']),
        (('(()(())((())))',), ['(()(())((())))']),
        (('( ) (( )) (( )( ))',), ['()', '(())', '(()())']),
        (('',), []),
        (('()',), ['()']),
    ],
    "humanEval_2": [
        ((3.5,), 0.5),
        ((1.33,), 0.33, 1e-6),
        ((123.456,), 0.456, 1e-6),
        ((0.9999,), 0.9999, 1e-6),
        ((10.0,), 0.0),
    ],
    "humanEval_3": [
        (([],), False),
        (([1, 2, -3, 1, 2, -3],), False),
        (([1, 2, -4, 5, 6],), True),
        (([1, -1, 2, -2, 5, -5, 4, -4],), False),
        (([1, -1, 2, -2, 5, -5, 4, -5],), True),
        (([100, -50, -60],), True),
        (([-1],), True),
        (([0],), False),
    ],
    "humanEval_4": [
        (([1.0, 2.0, 3.0],), 2.0 / 3.0, 1e-6),
        (([1.0, 2.0, 3.0, 4.0],), 1.0, 1e-6),
        (([1.0, 2.0, 3.0, 4.0, 5.0],), 6.0 / 5.0, 1e-6),
        (([1.0, 1.0, 1.0],), 0.0),
        (([10.0, 0.0],), 5.0),
        (([0.0, 0.0, 10.0],), 40 / 9, 1e-6),
    ],
    "humanEval_5": [
        (([], 7), []),
        (([5, 6, 3, 2], 8), [5, 8, 6, 8, 3, 8, 2]),
        (([2, 2, 2], 2), [2, 2, 2, 2, 2]),
        (([1], 9), [1]),
        (([1, 2], 0), [1, 0, 2]),
        ((list(range(5)), -1), [0, -1, 1, -1, 2, -1, 3, -1, 4]),
    ],
    "humanEval_6": [
        (('(()()) ((())) () ((())()())',), [2, 3, 1, 3]),
        (('() (()) ((())) (((())))',), [1, 2, 3, 4]),
        (('(()(())((())))',), [4]),
        (('',), []),
        (('()',), [1]),
        (('(((()))) (()())',), [4, 2]),
    ],
    "humanEval_7": [
        (([], 'john'), []),
        ((['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx'), ['xxx', 'xxxAAA', 'xxx']),
        ((['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx'), ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']),
        ((['grunt', 'trumpet', 'prune', 'gruesome'], 'run'), ['grunt', 'prune']),
        ((['apple', 'banana', 'grape'], 'a'), ['apple', 'banana', 'grape']),
        ((['apple', 'banana', 'grape'], 'z'), []),
        ((['', ' '], ''), ['', ' ']),
    ],
    "humanEval_8": [
        (([],), (0, 1)),
        (([1, 1, 1],), (3, 1)),
        (([100, 0],), (100, 0)),
        (([3, 5, 7],), (15, 105)),
        (([10],), (10, 10)),
        (([1, -1, 2, -2],), (0, 4)),
        (([1, 2, 3, 4, 5],), (15, 120)),
    ],
    "humanEval_9": [
        (([],), []),
        (([1, 2, 3, 4],), [1, 2, 3, 4]),
        (([4, 3, 2, 1],), [4, 4, 4, 4]),
        (([3, 2, 3, 100, 3],), [3, 3, 3, 100, 100]),
        (([-1, 2, 3],), [-1, 2, 3]),
        (([0, 0, 0, 0],), [0, 0, 0, 0]),
        (([1, 1, 2, 2, 1],), [1, 1, 2, 2, 2]),
        (([-5, -4, -3, -10],), [-5, -4, -3, -3]),
        (([10],), [10]),
        (([5, 10, 5, 10, 5, 10],), [5, 10, 10, 10, 10, 10]),
    ],
}

def check(candidate, question):
    test_cases = tests[question]
    passed = 0

    for i, case in enumerate(test_cases, start=1):
        if len(case) == 3:
            args, expected, tol = case
        else:
            args, expected = case
            tol = None

        try:
            result = candidate(*args)
            if tol is not None and isinstance(expected, float):
                assert abs(result - expected) < tol
            else:
                assert result == expected
        except AssertionError:
            print(f"{question}")
            print(f"Test {i} FAILED: input={args}, got {result}, expected {expected}")
        else:
            passed += 1

    total = len(test_cases)
    print(f"\nSummary: {passed}/{total} tests passed.")
    return passed == total

def check_solution(solution: dict, question: str) -> bool:
    namespace = {}
    code = solution[0]["code"]
    try:
        exec(code, namespace)
        
        return check(namespace["candidate"], question)
    except AssertionError:
        return False
    except Exception as e:
        print("Error during execution:", traceback.format_exc())
        return False

def test(model, strategy, s, f):
    total_p_pass = 0
    for i in range(s, f):
        with open(f'outputs/{model}/{strategy}/p{i}.json', 'r') as file:
            data = json.load(file)

            if check_solution(data, f'humanEval_{i}'):
                total_p_pass += 1
            print("\n")

    print('Total number of problems passed: ', total_p_pass)

def test_revised():
    with open(f'outputs/deepseek/CoT/revised_p8.json', 'r') as file:
        data = json.load(file)

        if(check_solution(data, f'humanEval_{8}')):
            print('deepseek revised_p8 passed')
        else:
            print('deepseek revised_p8 failed')
        print("\n")

    with open(f'outputs/llama/SCoT/revised_p1.json', 'r') as file:
        data = json.load(file)

        if(check_solution(data, f'humanEval_{1}')):
            print('llama revised_p1 passed')
        else:
            print('llama revised_p1 failed')
        print("\n")

def generate_innovated_outputs():
    for i in range(10):
        deepseek_innovated = extract_code_block(generate_code('deepseek', 'innovated', ques_num=i))
        llama_innovated = generate_code('llama', 'innovated', ques_num=i)

        save_output('deepseek', 'innovated', i, deepseek_innovated)
        save_output('llama', 'innovated', i, llama_innovated)