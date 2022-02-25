"""
163. Missing Ranges
https://leetcode.com/problems/missing-ranges/
Easy
"""

"""
thought process: 
1. compare first element with lower, if nums[0] > lower, gap = nums[0] - lower
2. append upper to nums
3. loop through i in range(1,len(nums))
4. if nums[i+1] - nums[i] > 1, missing range, gap = nums[i+1] - nums[i] - 1
5. use another function to construct the appending str

lower: 0, upper = 6, nums = [2,4,5] 
0->1, 3, 6
"""
from typing import List


class Solution:
    def gap_to_str(self, lb, ub):
        if lb == ub:
            return str(lb)
        else:
            return str(lb) + '->' + str(ub)

    def missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        nums.append(upper + 1)
        prev = lower - 1
        for i in range(len(nums)):
            curr = nums[i]
            if curr - prev > 1:
                ans.append(self.gap_to_str(prev + 1, curr - 1))
            prev = curr
        return ans
