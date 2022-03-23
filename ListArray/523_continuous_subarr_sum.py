"""
523. Continuous Subarray Sum (Medium)
https://leetcode.com/problems/continuous-subarray-sum/

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose
elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""
from typing import List


class Solution:
    def check_subarr_sum(self, nums: List[int], k: int) -> bool:
        comp = {0: -1}
        prev = 0
        for i, num in enumerate(nums):
            prev += num
            mul = prev % k
            if mul in comp and comp[mul] < i - 1:
                return True
            comp[mul] = i
        return False