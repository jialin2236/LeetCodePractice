"""
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in non-decreasing order,
 find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List, Tuple


# try binary search
def search_rng(nums: List[int], target: int) -> Tuple[int, int]:
    def find_bound(lower: bool) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i <= j:
            mid = (i + j) //2
            if nums[mid] == target:
                if lower:
                    if mid == i or nums[mid - 1] < target:
                        return mid
                    j = mid - 1
                else:
                    if mid == j or nums[mid + 1] > target:
                        return mid
                    i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1
    lower_bound = find_bound(True)
    if lower_bound == -1:
        return -1, -1
    upper_bound = find_bound(False)
    return lower_bound, upper_bound





