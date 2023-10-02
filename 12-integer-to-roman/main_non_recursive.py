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

        prefix = ""
        while num > bases[-1]:
            prefix += roman_map[bases[-1]]
            num = num - bases[-1]

        # Split number
        nums = []
        divider = 10
        while num // divider > 0:
            remainder = num % divider
            divider *= 10
            num = num - remainder
            if remainder:
                nums.append(remainder)
        nums.append(num)

        # Convert numbers and concat the results
        result = ""
        for num in nums:
            if num in roman_map:
                result = roman_map[num] + result
                continue

            base_idx = 0
            while base_idx < len(bases) and bases[base_idx] < num:
                base_idx += 1

            base = bases[base_idx]
            subtracting_base = bases[base_idx - (2 - (base_idx % 2))]

            if base - subtracting_base == num:
                result = (roman_map[subtracting_base] + roman_map[base]) + result
            else:
                num_as_roman = ""
                remainder_to_convert = num
                while remainder_to_convert > 0:
                    pre_base_idx = 0
                    while (
                        pre_base_idx + 1 < len(bases)
                        and bases[pre_base_idx + 1] <= remainder_to_convert
                    ):
                        pre_base_idx += 1

                    num_as_roman = num_as_roman + roman_map[bases[pre_base_idx]]
                    remainder_to_convert = remainder_to_convert - bases[pre_base_idx]
                result = num_as_roman + result

        return prefix + result


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
