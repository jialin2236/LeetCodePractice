"""
55. Jump Game
"""
from functools import lru_cache
from typing import List

# input nums: List[int]
# output bool 
# each ele ment in nums indicates the maximum number of steps you could jump from that index
# return if you could reach the last index from the first index

class Solution:
    def canJump_backtrack(self, nums: List[int]) -> bool: 
        res = False

        @lru_cache(None)
        def helper(idx): 
            if res: 
                return
            if idx == len(nums) - 1: 
                res = True
                return
            max_j = min(idx + nums[idx], len(nums) - 1)
            for j in range(idx + 1, max_j + 1): 
                helper(j)

        helper(0)
        return res

    def canJump_dp(self, nums: List[int]) -> bool: 
        # dp[i] - whether or not we can reach last index from index i
        # answer is dp[0]
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[n-1] = True
        for i in range(n-2, -1, -1): 
            if any([j for j in range(i + 1, n) if dp[j] and i + nums[i] >= j]): 
                dp[i] = True
        return dp[0]

    def canJump_iter(self, nums: List[int]) -> bool: 
        i = len(nums) - 1
        for j in range(i - 1, -1, -1): 
            if j + nums[j] >= i: 
                i = j
        return i == 0



    