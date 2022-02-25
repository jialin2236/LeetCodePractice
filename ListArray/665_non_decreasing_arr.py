"""
Given an array nums with n integers,
your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
such that (0 <= i <= n - 2).
"""

"""
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

nums = [1,2,8,4,5,6,7] -> [1,2,3,4,5,6,7]
nums = [1,2,3,1,5,6,7] -> [1,2,3,4,5,6,7]
nums = [1,4,2,3] -> [1,2,2,3]
"""
from typing import List

class Solution:
    def non_decr_arr(self, nums: List[int]) -> bool:
        n = len(nums)
        i, k = 0, 0
        while i < n-1:
            if nums[i] > nums[i+1]:
                if k > 0:
                    return False
                k += 1
                if i == 0 or nums[i-1] < nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
        return True