"""
410. Split Array Largest Sum (Hard)
https://leetcode.com/problems/split-array-largest-sum/

Given an array nums which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
"""
from typing import List

# example
# nums = [7,2,5,10,8], m = 2
# output: 18 -> [[7,2,5], [10,8]]

# if we split it into len(nums) sub-arrays (each element is its own sub-array), m = len(nums)
# max(sum(sub_arr)) = max(nums)
# if we don't split the array, the only sub-array being the array itself, m = 1
# max(sum(sub_arr)) = sum(nums)
# we need to search between [max(nums), sum(nums)], and find the minimum value that satisfy the condition
# (splitting array into at m sub-arrays)

class Solution:
    def split_arr(self, nums: List[int], m: int) -> int:
        def feasible(x: int) -> bool:
            # if a largest sum of x is feasible condition
            n_arr = 1
            arr_sum = 0
            for ele in nums:
                arr_sum += ele
                if arr_sum > x:
                    arr_sum = ele
                    n_arr += 1
                    if n_arr > m:
                        return False
            return True

        lb, ub = max(nums), sum(nums)
        while lb < ub:
            mid = lb + (ub - lb) // 2
            if feasible(mid):
                # mid is feasible, but not necessarily minimum -> try smaller value
                # since mid - 1 may not be feasible
                ub = mid
            else:
                # mid is not feasible -> dividing into too many sub-arrays -> mid too small -> try larger value
                # since mid is guaranteed not to be feasible
                lb = mid + 1
        return lb