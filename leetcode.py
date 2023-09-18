#!/usr/bin/env python
import sys
import pathlib

problem_name = sys.argv[1] if len(sys.argv) > 1 else input("Problem name: ")
path = pathlib.Path(problem_name)
path.mkdir(exist_ok=False)

script_content = """
TESTS = {
    (): [None]
}


class Solution:
    def method(self, ):
        pass


if __name__ == "__main__":
    solution = Solution()
    method = getattr(
        solution, list(filter(lambda m: not m.startswith("_"), dir(solution)))[0]
    )
    for _input, expected_output in TESTS.items():
        actual_output = method(*_input)
        if not isinstance(expected_output, list):
            expected_output = [expected_output]

        if actual_output in expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
"""

with open(str(path / "main.py"), "w") as f:
    f.write(script_content[1:])
