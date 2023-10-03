from typing import List

TESTS = {
    ("23",): [["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]],
    ("2",): [["a", "b", "c"]],
    ("",): [[]],
    ("234",): [
        [
            "adg",
            "adh",
            "adi",
            "aeg",
            "aeh",
            "aei",
            "afg",
            "afh",
            "afi",
            "bdg",
            "bdh",
            "bdi",
            "beg",
            "beh",
            "bei",
            "bfg",
            "bfh",
            "bfi",
            "cdg",
            "cdh",
            "cdi",
            "ceg",
            "ceh",
            "cei",
            "cfg",
            "cfh",
            "cfi",
        ]
    ],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Letter combinations of a phone number.

        https://leetcode.com/problems/letter-combinations-of-a-phone-number/
        """
        if not digits:
            return []

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i, current_string):
            if len(current_string) == len(digits):
                res.append(current_string)
                return

            for c in digit_map[digits[i]]:
                backtrack(i + 1, current_string + c)

        backtrack(0, "")
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
