"""
435. Non-overlapping Intervals (Medium, 6 fb tagged 0 - 6 months)
https://leetcode.com/problems/non-overlapping-intervals/

given an array of intervals, where intervals[i] = [start_i, end_i], return the minimum number of
intervals you need to remove to make the rest of the intervals non-overlapping
"""
from typing import List


# we can sort the intervals first by start_i
# if two neighboring intervals overlap
# 1. interval[i] is a subset of interval[i-1] (start[i] < end[i-1] and end[i] <= end[i-1])
#       -> remove interval[i-1], since it has larger coverage, hence higher chance of future overlap
# 2. overlap but not a subset (start[i] < end[i-1] and end[i] > end[i-1])
#       -> remove interval[i], since interval[i-1] has not overlap with previous intervals, and interval[i] has larger
#          upper bound, hence higher chance of future overlap
# -> if there is overlap, remove interval with higher upper bound

class Solution:
    def erase_overlap(self, intervals: List[List[int]]) -> int:
        """
        time: O(nlogn) - sorting + iteration
        space: O(1)
        :param intervals:
        :return:
        """
        intervals.sort()
        # latest upper bound of the stream of intervals
        curr = intervals[0][1]
        ans = 0
        for lb, ub in intervals[1:]:
            if lb <= curr:
                ans += 1
                curr = min(ub, curr)
        return ans
