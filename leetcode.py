#!/usr/bin/env python
import json
import pathlib
import re
import subprocess
import sys
import requests

problem_url = sys.argv[1] if len(sys.argv) > 1 else input("Problem URL: ")
recreate = (sys.argv[2] == "recreate") if len(sys.argv) > 2 else False
extra_imports = []


url_pattern = re.compile(
    r"https://leetcode.com/problems/(?P<title_slug>[a-z0-9_-]+)(/\w+)*"
)
match = url_pattern.match(problem_url)
if match:
    title_slug = match.group("title_slug")
else:
    print(f"Invalid URL. Must match: {url_pattern.pattern}")
    sys.exit(1)

query_info = {
    "query": (
        "\n    query questionTitle($titleSlug: String!) {\n  question(titleSlug: "
        "$titleSlug) {\n    questionId\n    questionFrontendId\n    title\n    "
        "titleSlug\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    "
        "categoryTitle\n  }\n}\n    "
    ),
    "variables": {"titleSlug": title_slug},
    "operationName": "questionTitle",
}
query_content = {
    "query": (
        "\n    query questionEditorData($titleSlug: String!) {\n  question(titleSlug: "
        "$titleSlug) {\n    questionId\n    questionFrontendId\n    codeSnippets "
        "{\n      lang\n      langSlug\n      code\n    }\n    "
        "envInfo\n    enableRunCode\n    hasFrontendPreview\n    frontendPreviews\n  "
        "}\n}\n    "
    ),
    "variables": {"titleSlug": title_slug},
    "operationName": "questionEditorData",
}
query_test_cases = {
    "query": (
        "\n    query consolePanelConfig($titleSlug: String!) {\n  question(titleSlug: "
        "$titleSlug) {\n    "
        "questionId\n    questionFrontendId\n    questionTitle\n    enableDebugger"
        "\n    enableRunCode\n    enableSubmit\n    enableTestMode"
        "\n    exampleTestcaseList\n    metaData\n  }\n}\n    "
    ),
    "variables": {"titleSlug": title_slug},
    "operationName": "consolePanelConfig",
}


print("Getting basic info...")
response = requests.post("https://leetcode.com/graphql/", json=query_info)
response.raise_for_status()
data = response.json()
number = data["data"]["question"]["questionId"]
title_slug = data["data"]["question"]["titleSlug"]
title = data["data"]["question"]["title"]

print("Getting code snippet...")
response = requests.post("https://leetcode.com/graphql/", json=query_content)
response.raise_for_status()

data = response.json()
snippets = data["data"]["question"]["codeSnippets"]
python_snippet = next(filter(lambda d: d["langSlug"] == "python3", snippets))["code"]
if "List[" in python_snippet:
    extra_imports.append("from typing import List")

print("Getting test cases...")
response = requests.post("https://leetcode.com/graphql/", json=query_test_cases)
response.raise_for_status()
data = response.json()
test_cases = data["data"]["question"]["exampleTestcaseList"]
tests = []
for test_case in test_cases:
    params = "(" + ", ".join(test_case.split("\n")) + ")"
    tests.append(f'{{"in": {params}, "out": ...}},')
tests_str = "\n    ".join(tests)

metadata = json.loads(data["data"]["question"]["metaData"])
method_name = metadata["name"]


script_content = """
{extra_imports_str}
TESTS = [
    {tests}
]


{snippet}pass


if __name__ == "__main__":
    for test_case in TESTS:
        _input = test_case["in"]
        expected_output = test_case["out"]
        actual_output = Solution().{method_name}(*_input)

        if actual_output == expected_output:
            print(f"[OK] {{_input}} -> {{actual_output}}")
        else:
            print(f"[XX] {{_input}} -> {{actual_output}} (expected: {{expected_output}})")
"""  # noqa

path = pathlib.Path(number + "-" + title_slug)
path.mkdir(exist_ok=recreate)

content = script_content[1:].format(
    method_name=method_name,
    snippet=python_snippet,
    tests=tests_str,
    extra_imports_str="\n".join(extra_imports) + "\n",
)
with open(str(path / "main.py"), "w") as f:
    f.write(content)

subprocess.call(["black", str(path)])
