"""
523. Continuous Subarray Sum (Medium, 50 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/continuous-subarray-sum/

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose
elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""
from typing import List

# if two numbers (index i, j) in array have the same remaining when divided by k, the nums[i] - nums[j]
# is divisible by k
# k = 3, num_1 = 5, num_2 = 14
# num_1 % k = 5 % 3 = 2, num_2 % k = 14 % 3 = 2 -> (14 - 5) = 9 % 3 = 0
# m1 * 3 + 2 = num_1, m2 * 3 + 2 = num_2 -> num2 - num1 = 3 * (m2 - m1)
# since m2 = some_int, m1 = some_int, num2 - num1 = some_int * 3

class Solution:
    def check_subarr_sum(self, nums: List[int], k: int) -> bool:
        comp = {0: -1}
        prev = 0
        for i, num in enumerate(nums):
            prev += num
            mul = prev % k
            if mul not in comp:
                comp[mul] = i
            elif comp[mul] < i - 1:
                return True
        return False

