TESTS = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "VI": 6,
    "IX": 9,
    "XII": 12,
    "XX": 20,
    "LVIII": 58,
    "CDXCVIII": 498,
    "CMXCIV": 994,
    "M": 1000,
    "MCMXCIV": 1994,
    "MMMCMXCIX": 3999,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Roman to integer.
        https://leetcode.com/problems/roman-to-integer/
        """
        symlist = [
            ("I", 1),
            ("IV", 4),
            ("V", 5),
            ("IX", 9),
            ("X", 10),
            ("XL", 40),
            ("L", 50),
            ("XC", 90),
            ("C", 100),
            ("CD", 400),
            ("D", 500),
            ("CM", 900),
            ("M", 1000),
        ]
        res = 0
        for sym, val in reversed(symlist):
            while s.startswith(sym):
                res += val
                s = s[len(sym) :]
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
