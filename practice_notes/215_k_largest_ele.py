"""
215. Kth largest element in an array
https://leetcode.com/problems/kth-largest-element-in-an-array
Medium

Given a number array nums, and an integer k. Return the Kth largest element in array nums
"""
import random

"""
Ideas: 
1. use quick select
2. use a heap
Question: 
1. are all elements positive? 
2. what to return if k > length of array? 
"""
from typing import List, Optional


class Solution:
    def partition(self, nums, start, end, pvt_idx):
        for i in range(start, end+1):
            if i == pvt_idx:
                nums[i], nums[end] = nums[end], nums[i]
                break
        pivot = nums[end]
        i = start
        for j in range(start, end):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i

    def quick_select(self, nums, start, end, k):
        idx = random.randint(start, end)
        pi = self.partition(nums, start, end, idx)
        if pi - start == k - 1:
            return nums[pi]
        if pi - start < k - 1:
            # less than k elements larger than nums[pi]
            self.quick_select(nums, pi + 1, end, k - 1 - pi + start)
        else:
            self.quick_select(nums, start, pi - 1, k)

    def k_largest(self, nums: List[int], k: int) -> Optional[int]:
        n = len(nums)
        if k > n:
            return
        ans = self.quick_select(nums, 0, n - 1, k)

    def kth_largest(self, nums: List[int], k: int) -> Optional[int]:
        if not nums:
            return
        pivot = nums[random.randint(0, len(nums)-1)]
        left = [ele for ele in nums if ele < pivot]
        mid = [ele for ele in nums if ele == pivot]
        right = [ele for ele in nums if ele > pivot]

        if k < len(left):
            return self.kth_largest(left, k)
        elif k > len(left) + len(mid):
            return self.kth_largest(right, k - len(left) - len(mid))
        else:
            return mid[0]
