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
        prefix = ""
        while num >= 1000:
            prefix += "M"
            num = num - 1000

        units = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
        }
        decimals = {
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC",
        }
        hundreds = {
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM",
        }

        digits = []
        while num // 10 > 0:
            digits.append(num % 10)
            num //= 10
        digits.append(num % 10)

        res = ""
        for i, digit in enumerate(digits):
            if digit == 0:
                continue
            res = [units, decimals, hundreds][i][digit] + res
        return prefix + res


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
