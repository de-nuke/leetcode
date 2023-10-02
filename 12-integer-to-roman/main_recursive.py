from collections import OrderedDict
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
    1994: "MCMXCIV",
    3999: "MMMCMXCIX",
}


class Solution:
    @lru_cache
    def intToRoman(self, num: int) -> str:
        """Integer to roman"""
        roman_map = OrderedDict(
            [
                (1, "I"),
                (5, "V"),
                (10, "X"),
                (50, "L"),
                (100, "C"),
                (500, "D"),
                (1000, "M"),
            ]
        )
        bases = list(roman_map.keys())

        if num > bases[-1]:
            return self.intToRoman(bases[-1]) + self.intToRoman(num - bases[-1])

        if num in roman_map:
            return roman_map[num]

        divider = 1
        while num // divider > 0:
            divider *= 10
        divider = divider // 10

        remainder = num % divider
        num = num - remainder

        if remainder == 0:
            base_idx = 0
            while base_idx < len(bases) and bases[base_idx] < num:
                base_idx += 1
            base = bases[base_idx]
            subtracting_base = bases[base_idx - (2 - (base_idx % 2))]

            if base - subtracting_base == num:
                return roman_map[subtracting_base] + roman_map[base]
            else:
                return roman_map[bases[base_idx - 1]] + self.intToRoman(
                    num - bases[base_idx - 1]
                )

        else:
            return self.intToRoman(num) + self.intToRoman(remainder)


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
