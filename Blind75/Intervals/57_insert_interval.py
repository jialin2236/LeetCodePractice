"""
57. Insert Interval (Medium, 4 fb tagged 0-6 months)
https://leetcode.com/problems/insert-interval/

given an array of non-overlapping intervals intervals, intervals[i] = [start_i, end_i]
is sorted in ascending order by start_i. Also given a newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i,
and does not have any overlapping intervals. Return intervals after insertion
"""
from typing import List

# since start_i is already sorted, we can search the current array (linearly), and find
# an interval that overlaps with newInterval, or closest to it.

# example = [[1,3], [6,9]], newInterval = [2,5] -> [[1,5], [6,9]]
# 2 scenarios
# 1. there's overlap of an interval with newInterval
# 2. there's no overlap of any interval with newInterval
# criteria of overlap
# - start < end_i
# - AND end > start_i
# initiate a new array ans = [intervals[0]]
# iterate through intervals, compare it with ans[-1]
# 1. if start_i < start and end_i < start -> append intervals[i]
# 2. if start < start_i and end < start_i -> append newInterval
# 3. if start < end_i AND end > start_i -> OVERLAP -> append [min(start, start_i), max(end, end_i)]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        time: O(N) - iterating through intervals
        space: O(N) - storing the answer
        :param intervals:
        :param newInterval:
        :return:
        """
        ans = []
        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                ans.append(interval)
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[idx:]
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        ans.append(newInterval)
        return ans

    def insert_merge(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        time: O(nlogn)
        space: O(n) for storing answer 
        :param intervals:
        :param newInterval:
        :return:
        """
        intervals.append(newInterval)
        ans = []
        for interval in sorted(intervals):
            if interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans