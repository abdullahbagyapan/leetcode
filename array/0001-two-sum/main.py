from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        return []


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    for idx, (nums, target, expected) in enumerate(test_cases, start=1):
        result = sol.twoSum(nums, target)
        assert result == expected, f"Test {idx} failed: got {result}, expected {expected}"
        print(f"Test {idx} passed: {result}")