from huggingface_hub import InferenceClient
import os
import json

client = InferenceClient(
    provider="novita",
)

MODEL = 'meta-llama/Llama-3.1-8B-Instruct'

def generation(question_number):
    file_path = os.path.join("problems", f"{question_number}.json")

    problem_statement = ""
    method_signature = ""

    with open(file_path, 'r') as file:
        data = json.load(file)
        problem_statement = data["problem_statement"]
        method_signature = data["method_signature"]

    PROMPT = f'''
Problem description:
{problem_statement}

Method signature:
{method_signature}

Please write formal specifications as Python assert statements that describe the 
correct behavior of this method.

Let "res" denote the expected return value of candidate(numbers). 
Do NOT call candidate() inside the assertions.
Do NOT use any methods that cause side effects such as:
- modifying lists or data structures (append, add, remove, setitem)
- printing or I/O (print, input, file operations)
- randomness or timing (random, datetime.now)

Use only pure arithmetic, boolean logic, and immutable expressions.
The assertions must describe logical relationships between the input list,
the mean of the list, the absolute deviations, and the final MAD value.

Produce approximately 5 unique specification-style assertions.
Return ONLY Python assert statements (no prose, no comments).
'''
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": PROMPT
            }
        ],
    )

    content = completion.choices[0].message.content

    dir_path = os.path.join("outputs")
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "testcases", f"{question_number}.json")

    data = [
        {'code': content}
    ]
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

generation("q4")
generation("q9")