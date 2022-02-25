"""
11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""
from typing import List

# 1
# traverse through the list and update max area
# output such
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        ans = 0
        while i < j:
            area = min(nums[i], nums[j]) * (j - i)
            if area > ans:
                ans = area
            if nums[i] < nums[j]:
                i += 1
            else:
                j -= 1
        return ans 
