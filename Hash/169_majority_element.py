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

# Boyer-Moore Voting Algorithm
#
# Intuition
# If we had some way of counting instances of the majority element as +1
# and instances of any other element as -1,
# summing them would make it obvious that the majority element is indeed
# the majority element.
#
# Algorithm
# Essentially, what Boyer-Moore does is look for a suffix suf
# of nums where suf[0] is the majority element in that suffix.
# To do this, we maintain a count,
# which is incremented whenever we see an instance of our current candidate
# for majority element and decremented whenever we see anything else.
# Whenever count equals 0,
# we effectively forget about everything in nums up to the current index
# and consider the current number as the candidate for majority element.

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
