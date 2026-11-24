from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the shorter array to guarantee O(log(min(m, n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # elements taken from nums1
            j = half - i             # elements taken from nums2

            nums1_left = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right = nums1[i] if i < m else float("inf")
            nums2_left = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right = nums2[j] if j < n else float("inf")

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2 == 1:
                    return float(max(nums1_left, nums2_left))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1

        raise ValueError("Input arrays are not sorted.")


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([], [1], 1.0),
        ([0, 0], [0, 0], 0.0),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 5.5),
    ]

    for idx, (nums1, nums2, expected) in enumerate(test_cases, start=1):
        result = sol.findMedianSortedArrays(nums1, nums2)
        assert result == expected, f"Test {idx} failed: got {result}, expected {expected}"
        print(f"Test {idx} passed: {result}")