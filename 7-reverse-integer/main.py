TESTS = {
    (123,): [321],
    (-123,): [-321],
    (120,): [21],
    (1,): [1],
    (-1,): [-1],
    (0,): [0],
    (-100000,): [-1],
    (2**31 - 1,): [0],
    (-(2**31),): [0],
}


class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse Integer
        https://leetcode.com/problems/reverse-integer/
        """
        min_int = -(2**31)
        max_int = 2**31 - 1

        sign = -1 if x < 0 else 1

        x = abs(x)

        res = 0
        while x > 0:
            res = res * 10 + (x % 10)
            x = x // 10

        res = res * sign
        if res > max_int or res < min_int:
            return 0
        return res


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
