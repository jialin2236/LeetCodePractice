"""
452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Medium
"""
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        curr_e = points[0][1]
        for s, e in points[1:]:
            if s > curr_e:
                arrows += 1
                curr_e = e
        return arrows
    