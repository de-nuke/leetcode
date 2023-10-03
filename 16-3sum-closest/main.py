import math
from typing import List

TESTS = {
    ((-1, 2, 1, -4), 1): 2,
    ((0, 0, 0), 1): 0,
}


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """Three Sum Closes

        https://leetcode.com/problems/3sum-closest/.

        Based on 3Sum solution from YouTube: https://www.youtube.com/watch?v=jzZsG8n2R9A
        """
        nums = list(nums)
        nums.sort()
        best_diff = math.inf
        best_three_sum = None

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > target:
                    r -= 1
                elif three_sum < target:
                    l += 1
                else:
                    return three_sum

                diff = abs(target - three_sum)
                if diff < best_diff:
                    best_diff = diff
                    best_three_sum = three_sum
        return best_three_sum


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
