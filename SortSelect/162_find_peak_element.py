"""
162. Find Peak Element
https://leetcode.com/problems/find-peak-element
Medium

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
"""
from typing import List

class Solution:
    def peak_element(self, nums: List[int]) -> int:
        """
        binary search to look for increasing sequence
        :param nums:
        :return:
        """
        i, j = 0, len(nums) - 1
        # when j - i + 1 >= 3, we can do binary search (i < j - 1)
        # otherwise, if length == 2 and nums[i] > nums[j], return i
        # if length == 1, return i
        while i < j - 1:
            mid = (i + j) // 2
            if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]: 
                return mid
            elif nums[mid] < nums[mid + 1]: 
                # peak element is on right side of mid
                i= mid + 1
            else: 
                # peak element is on left side of mid
                j = mid - 1
        # if j - i + 1 <= 2, nums = [n1, n2] or nums = [n1]
        return i if nums[i] >= nums[j] else j