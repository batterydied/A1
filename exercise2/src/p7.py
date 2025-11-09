from typing import List

def candidate(strings: list[str], substring: str) -> list[str]:
    return [s for s in strings if substring in s]
