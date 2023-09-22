TESTS = {((1, 8, 6, 2, 5, 4, 8, 3, 7),): 49, ((1, 1),): 1}


class Solution:
    def maxArea(self, height: list) -> int:
        """
        Container with most water.
        https://leetcode.com/problems/container-with-most-water/

        Solution found here: https://www.geeksforgeeks.org/container-with-most-water/
        """
        n = len(height)
        i = 0
        j = n - 1
        max_area = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return max_area


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
