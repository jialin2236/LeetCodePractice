from typing import List
# intervals are not sorted

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        n_int = len(intervals) - 1
        for i in range(1, n_int):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            elif intervals[i][1] > result[-1][1]:
                result[-1][1] = intervals[i][1]
        return result

    def merge0(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i][0] > intervals[i-1][1]:
                i += 1
            else:
                curr_rng = intervals.pop(i)
                intervals[i-1][1] = max(intervals[i-1][1], curr_rng[1])
        return intervals




