from functools import lru_cache

TESTS = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    6: "VI",
    9: "IX",
    12: "XII",
    20: "XX",
    58: "LVIII",
    498: "CDXCVIII",
    994: "CMXCIV",
    1000: "M",
    1994: "MCMXCIV",
    3999: "MMMCMXCIX",
}


class Solution:
    @lru_cache
    def intToRoman(self, num: int) -> str:
        """Integer to roman"""
        symlist = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M"),
        ]

        res = ""
        for val, sym in reversed(symlist):
            if num // val:
                count = num // val
                res = res + (sym * count)
                num = num % val
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
