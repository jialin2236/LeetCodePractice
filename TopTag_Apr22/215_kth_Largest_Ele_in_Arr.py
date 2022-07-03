"""
125. Kth Largest Element in an Array (M, 119)
"""
from typing import List
import random
import heapq

class Solution:
    def kth_largest_qs(self, nums: List[int], k: int) -> int:
        """
        time: O(N) avg, O(N^2) worst
        space: O(1)
        :param nums:
        :param k:
        :return:
        """
        def partition(left, right, pidx):
            nums[pidx], nums[right] = nums[right], nums[pidx]
            pivot, i = nums[right], left
            for j in range(left, right):
                if nums[j] > pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i

        def quick_select(start, end, ki):
            pi = partition(start, end, random.randint(start, end))
            if pi - start + 1 == ki:
                return pi
            elif pi - start + 1 > ki:
                return quick_select(start, pi - 1, ki)
            else:
                return quick_select(pi + 1, end, ki + start - pi - 1)

        ans = quick_select(0, len(nums) - 1, k)
        return nums[ans]

    def kth_largest_heap(self, nums: List[int], k: int) -> int:
        """
        time: O(N + klogN)
        space: O(N)
        :param nums:
        :param k:
        :return:
        """
        nums = [-ele for ele in nums]
        heapq.heapify(nums)
        for i in range(k):
            ele = heapq.heappop(nums)
        return -ele
