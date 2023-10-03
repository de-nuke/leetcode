#!/usr/bin/env python
import sys
import pathlib

problem_name = sys.argv[1] if len(sys.argv) > 1 else input("Problem name: ")
method_name = sys.argv[2] if len(sys.argv) > 2 else input("Method name: ")
path = pathlib.Path(problem_name)
path.mkdir(exist_ok=False)

script_content = """
TESTS = {{
    (): [None]
}}


class Solution:
    def {method_name}(self, ):
        \"\"\"{problem_name}\"\"\"
        pass


if __name__ == "__main__":
    solution = Solution()
    method = getattr(
        solution, list(filter(lambda m: not m.startswith("_"), dir(solution)))[0]
    )
    for _input, expected_output in TESTS.items():
        if not isinstance(_input, (tuple, list)):
            _input = (_input,)
        actual_output = method(*_input)
        if not isinstance(expected_output, list):
            expected_output = [expected_output]

        if actual_output in expected_output:
            print(f"[OK] {{_input}} -> {{actual_output}}")
        else:
            print(f"[XX] {{_input}} -> {{actual_output}} (expected: {{expected_output}})")
"""  # noqa

content = script_content[1:].format(
    method_name=method_name,
    problem_name=(problem_name.split("-", 1)[1].replace("-", " ").capitalize()),
)
with open(str(path / "main.py"), "w") as f:
    f.write(content)
