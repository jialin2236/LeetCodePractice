"""
252. Meeting Rooms (Easy, 2 fb tagged 0-6 months)
https://leetcode.com/problems/meeting-rooms/

given an array of meeting time intervals, intervals[i] = [start_i, end_i], determine if a person
could attend all meetings
"""
from typing import List

# ultimately, we need to determine if intervals contain any overlap
# sort intervals
# iterate through intervals
# of intervals[i][0] < intervals[-1][1] -> False
# else end of loop -> True


class Solution:
    def can_attend(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        n = len(intervals)
        for i in range(1, n):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True