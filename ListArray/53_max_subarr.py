"""
53. Maximum Subarray (Easy, 9 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""
from typing import List

# we iterate through the array
# at each step, there are 2 options
# 1. we extend the current window (sub-array)
# 2. we start a new window (sub-array)
# if including the previous window increases the sum, then we include it
# otherwise (if the single new element has a higher value), we start a new sub-array

class Solution:
    def max_sub_arr(self, nums: List[int]) -> int:
        curr = max_a = nums[0]
        for num in nums[1:]:
            curr = max(curr + num, num)
            max_a = max(max_a, curr)
        return max_a
