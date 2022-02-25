"""
674. Longest Continuous Increasing Subsequence
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence
(i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r)
such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
"""

"""
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
"""
from typing import List


class Solution:
    def longest_incr_subseq(self, nums: List[int]) -> int:
        """
        Time: O(N) - worst
        Space: O(1)
        :param nums:
        :return:
        """
        left, ans = 0, 0
        for i in range(1,len(nums)):
            if not nums[i-1] < nums[i]:
                left = i
            ans = max(ans, i - left + 1)
        return ans

    def longest_incr_subseq1(self, nums: List[int]) -> int:
        i = j = ans = 0
        while j < len(nums) - ans:
            ans = max(ans, j - i + 1)
            if not nums[j] < nums[j+1]:
                i = j + 1
            j += 1