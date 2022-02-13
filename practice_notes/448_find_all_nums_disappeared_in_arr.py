"""
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
"""
from typing import List

class Solution:
    def findDNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hashmap = {}
        ans = []
        # if we do not create a hash map and use
        # for i in range(1,n+1):
        #       if i not in nums:
        #           ans.append(i)
        # if i not in nums is another loop through nums (n)
        # total complexity is n^2, NOT FEASIBLE
        for i in range(n):
            hashmap[nums[i]] = 1

        for num in range(1, n+1):
            if num not in hashmap:
                ans.append(num)
        return ans

    def findDNums1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            idx = abs(nums[i]) - 1
            nums[idx] *= (-1 if nums[idx] > 0 else 1)
        ans = []
        for i in range(1, n+1):
            if nums[i-1] > 0:
                ans.append(nums[i])
        return ans