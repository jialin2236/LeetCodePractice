"""
523. Continuous SubArray Sum (M, 56)
"""
from typing import List

# given nums: List[int], k: int
# bool: if nums has a continuous subarray (2+ length) sum up to a multiple of k
# -> there exists i, j (i != j), sum(nums[i:j+1]) % k = 0

# if sum(nums[:i]) and sum(nums[:j+1]) has the same % k
# sum(nums[i:j+1]) % k = 0

class Solution:
    def check_subarr_sum(self, nums: List[int], k: int) -> bool:
        nums_mod = {0: -1}
        agg_sum = 0
        for i, ele in enumerate(nums):
            agg_sum += ele
            curr_mod = agg_sum % k
            if curr_mod in nums_mod and nums_mod[curr_mod] < i - 1:
                return True
            nums_mod[curr_mod] = i
        return False
