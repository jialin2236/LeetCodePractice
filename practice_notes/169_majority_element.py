"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

"""
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        time: O(n)
        space: O(1)
        :param nums:
        :return:
        """
        count = 0
        candidate = None
        size = len(nums)

        for n in nums:
            if not count:
                candidate = n
            count += (1 if n == candidate else -1)
            if count > size//2:
                return candidate

        return candidate

    def majorityElement0(self, nums: List[int]) -> int:
        """
        time: O(n)
        space: O(n)
        :param nums:
        :return:
        """
        count = {}
        threshold = len(nums)//2
        
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
            if count[n] > threshold:
                return n
