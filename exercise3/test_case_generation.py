from huggingface_hub import InferenceClient
import os
import json

client = InferenceClient(
    provider="novita",
)

MODEL = 'meta-llama/Llama-3.1-8B-Instruct'

def generation(question_number):
    file_path = os.path.join("specs", f"{question_number}.json")

    specs = ""

    with open(file_path, 'r') as file:
        data = json.load(file)
        specs = data["specs"]

    PROMPT = f'''
You are generating spec-guided unit tests.

Below are the final, corrected formal specifications of the function `candidate(numbers)`:

{specs}

Using only these specifications, generate pytest test cases that:

1. Call the function `candidate(numbers)` to compute `res`.
2. Construct input lists whose outputs can be inferred from the specifications.
3. Compute the expected result explicitly from the specification, not by using the function.
4. Assert that the function output matches the mathematically expected result.
5. Do not rewrite the specifications as test assertions.
6. Do not hardcode `res` manually.
7. Return only valid Python test code (no comments, no markdown).
8. Label every test function name with the prefix `test_spec_guided_`.

The output must consist of properly structured pytest test functions that exercise the actual implementation.
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
    file_path = os.path.join(dir_path, "test_cases", f"{question_number}.json")

    data = [
        {'code': content}
    ]
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

generation("q4")
generation("q9")