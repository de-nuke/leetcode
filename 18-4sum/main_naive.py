from typing import List

TESTS = [
    {
        "in": ([1, 0, -1, 0, -2, 2], 0),
        "out": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
    },
    {"in": ([2, 2, 2, 2, 2], 8), "out": [[2, 2, 2, 2]]},
]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            val = nums[i]
            if i > 0 and val == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                val2 = nums[j]
                if j > i + 1 and val2 == nums[j - 1]:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    three_sum = nums[j] + nums[i] + nums[l] + nums[r]
                    if three_sum > target:
                        r -= 1
                    elif three_sum < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return res


if __name__ == "__main__":
    for test_case in TESTS:
        _input = test_case["in"]
        expected_output = test_case["out"]
        actual_output = Solution().fourSum(*_input)

        if actual_output == expected_output:
            print(f"[OK] {_input} -> {actual_output}")
        else:
            print(f"[XX] {_input} -> {actual_output} (expected: {expected_output})")
