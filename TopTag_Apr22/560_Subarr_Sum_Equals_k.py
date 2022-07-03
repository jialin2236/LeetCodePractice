"""
560. Subarray Sum Equals K (M, 158)
"""
from typing import List

# what we know
# input - nums: List[int], k: int
# return number of subarrays whose sum equals to k

# nums = [1,1,1], k = 2 -> 2
# but nums[i] could be negative
# nums = [-1, 1, 1], k = 2 -> 2

# Approach
# use cumulative sum?
# nums = [-4, 2, -3, 1, 2, 4], k = 3
# csum = [-4, -2, -5, -4, -2, 2]
# if (cumulative_sum - k) in cumulative_sum_hash: ans += cumulative_sum_hash[cumulative_sum - k]
# since there could be multiple subarr having such cumulative sum
# [1, 1, -1, -1, 2, 4], k = 4

class Solution:
    def subarray_sum(self, nums: List[int], k: int) -> int:
        agg_sum_count = {0: 1}
        agg_sum = 0
        ans = 0
        for num in nums:
            agg_sum += num
            if agg_sum - k in agg_sum_count:
                ans += agg_sum_count[agg_sum - k]
            if agg_sum not in agg_sum_count:
                agg_sum_count[agg_sum] = 0
            agg_sum_count[agg_sum] += 1
        return ans