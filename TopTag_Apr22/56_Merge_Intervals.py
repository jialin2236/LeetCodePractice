"""
56. Merge Intervals (M, 106)
"""

# given a list of intervals: List[List[int]], intervals[i] = [start_i, end_i]
# merge all overlapping intervals, return non-overlapping intervals in an array

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if input array is not yet sorted, we need to sort it in order to linearly examine
        # any overlapping array
        intervals.sort()
        n, res = len(intervals), [intervals[0]]
        for i in range(1, n):
            start, end = intervals[i]
            prev_start, prev_end = res[-1]
            if start <= prev_end:
                # there is overlap
                new_end = max(prev_end, end)
                res[-1][1] = new_end
            else:
                res.append([start, end])
        return res 