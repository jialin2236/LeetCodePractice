"""
347. Top K Frequent Elements
Medium


Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
import collections
from typing import List, Dict, Counter
from collections import Counter
from random import randint

class Solution:
    def quick_select(self, counter: Counter, unique: List[int], left: int, right: int, k: int):
        def partition(pivot_idx: int):
            for i in range(len(unique)):
                if i == pivot_idx:
                    unique[right], unique[i] = unique[i], unique[right]
                    break
            pivot_num = unique[right]
            pivot_cnt = counter[pivot_num]
            i = left
            for j in range(left, right):
                num = unique[j]
                cnt = counter[num]
                if cnt < pivot_cnt:
                    unique[j], unique[i] = unique[i], unique[j]
                    i += 1
            unique[right], unique[i] = unique[i], unique[right]
            return i

        if left < right:
            idx = randint(left, right)
            pi = partition(idx)
            # numbers in unique[:pi-left+1] has less count than unique[pi]
            # numbers in unique[pi-left+1:] has more count than unique[pi]
            if pi - left + 1 == k:
                return unique[:pi]
            if pi - left + 1 > k:
                # pi is too large
                return self.quick_select(counter, unique, left, pi - 1, k)
            else:
                # pi is too small, we need k - pi + left - 1 more
                return self.quick_select(counter, unique, pi + 1, right, k - pi + left - 1)

    def top_k_freq(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        # intellij says error, but no error (tested)
        unique = list(cnt.keys())
        return self.quick_select(cnt, unique, 0, len(unique) - 1, k)
