TESTS = {
    ("42",): [42],
    ("   -42",): [-42],
    ("4193 with words",): [4193],
    ("--42",): [0],
    ("  only words",): [0],
    ("-2147483650",): [-2147483648],
    ("2147483650",): [2147483647],
    ("42   10",): [42],
    ("+    41",): [0],
    ("", ): [0]
}


class Solution:
    def myAtoi(self, s: str) -> int:
        """
        String to integer atoi
        https://leetcode.com/problems/string-to-integer-atoi/
        """
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        sign = 1
        reads_digits = False
        res = 0
        ord_0 = ord("0")
        for char in s:
            if char in digits:
                reads_digits = True
                digit = ord(char) - ord_0
                res = res * 10 + digit
            elif not reads_digits:
                if char == " ":
                    continue
                elif char in {"-"}:
                    reads_digits = True
                    sign = -1
                elif char in {"+"}:
                    reads_digits = True
                    sign = 1
                else:
                    break
            else:
                break
        return max(-(2**31), min(res * sign, 2**31 - 1))


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
