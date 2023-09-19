TESTS = {121: True, -121: False, 10: False, 0: True, 123454321: True, 1111151111: False}


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Palindrome number
        https://leetcode.com/problems/palindrome-number/
        """
        if x < 0:
            return False

        digits = []
        while x != 0:
            digits.append(x % 10)
            x //= 10
        return digits == digits[::-1]


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
