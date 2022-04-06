"""
56. Merge Intervals (Medium, 108 fb tagged 0-6 months)
https://leetcode.com/problems/merge-intervals/

given an array of intervals, intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all intervals in the input
"""
from typing import List


# if given array is not sorted, we can sort it first
# initiate ans to store output
# it is then guaranteed that intervals[i-1][0] <= intervals[i][0]
# iterate through the array, if there is overlap with latest element of ans (end >= start_i)
# replace latest element's upper bound with max(old ub, intervals[i][1])

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for lb, ub in intervals:
            if ans[-1][1] < lb:
                ans.append([lb, ub])
            else:
                ans[-1][1] = max(ub, ans[-1][1])
        return ans