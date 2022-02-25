"""
435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/

Medium
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_s, prev_e = intervals[0]
        ans = 0
        for s, e in intervals[1:]:
            if s >= prev_e:
                # no overlap
                prev_s, prev_e = s, e
                continue
            if e <= prev_e:
                # [s,e] is a subset of [prev_s, prev_e]
                # remove larger interval
                prev_s, prev_e = s, e
                # else e > prev_e
                # keep prev for a smaller ub
            ans += 1
        return ans
