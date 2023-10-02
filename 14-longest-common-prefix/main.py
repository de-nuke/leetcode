from typing import List

TESTS = {
    (("flower", "flow", "flight"),): "fl",
    (("dog", "racecar", "car"),): "",
    (("automobil", "automat", "autodrom"),): "auto",
    (("a",),): "a",
    ((),): "",
    (("cir", "car"),): "c",
}


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Longest common prefix.

        https://leetcode.com/problems/longest-common-prefix/
        """
        res = ""
        for vals in zip(*strs):
            if len(set(vals)) == 1:
                res += vals[0]
            else:
                break
        return res


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
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
