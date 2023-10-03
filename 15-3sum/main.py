from typing import List

TESTS = {
    ((-1, 0, 1, 2, -1, -4),): [[-1, -1, 2], [-1, 0, 1]],
    ((0, 1, 1),): [],
    ((0, 0, 0),): [[0, 0, 0]],
    ((-2, 0, 2, 0, 1, -1),): [[-2, 0, 2], [-1, 0, 1]],
}


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Three Sum

        https://leetcode.com/problems/3sum/.

        Solution found on YouTube: https://www.youtube.com/watch?v=jzZsG8n2R9A
        """
        nums = list(nums)
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
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

        if actual_output == expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
