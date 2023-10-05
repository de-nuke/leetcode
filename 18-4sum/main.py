from typing import List

TESTS = [
    {
        "in": ([1, 0, -1, 0, -2, 2], 0),
        "out": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
    },
    {"in": ([2, 2, 2, 2, 2], 8), "out": [[2, 2, 2, 2]]},
]


class Solution:
    def two_sum(self, nums, target):
        res = []
        left = 0
        right = len(nums) - 1

        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum > target:
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                res.append([nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
        return res

    def k_sum(self, nums, target, k):
        n = len(nums)
        res = []

        if k == 2:
            return self.two_sum(nums, target)

        for i in range(n):
            val = nums[i]
            if i > 0 and val == nums[i - 1]:
                continue

            results = self.k_sum(nums[i + 1 :], target - nums[i], k=k - 1)
            for result in results:
                res.append([nums[i], *result])
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.k_sum(nums, target, k=4)


if __name__ == "__main__":
    for test_case in TESTS:
        _input = test_case["in"]
        expected_output = test_case["out"]
        actual_output = Solution().fourSum(*_input)

        if actual_output == expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
