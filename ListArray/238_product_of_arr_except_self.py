"""
238. Product of Array Except Self (Medium, 19 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
from typing import List

# similar to trapping rain water
# we can approach it from both ends
# arr = [a, b, c, d, e]
# ans = [bcde, acde, abde, abce, abcd]
# cumulative product from left = [1, a, ab, abc, abcd]
# cumulative product from right = [bcde, cde, de, e, 1]

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        ans = [1]
        n = len(nums) - 1
        for i in range(n):
            pi = ans[-1] * nums[i]
            ans.append(pi)

        r_val = 1
        for j in range(n, -1, -1):
            ans[j] *= r_val
            r_val *= nums[j]
        return ans
