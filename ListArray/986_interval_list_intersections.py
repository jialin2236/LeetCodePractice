"""
986. Interval List Intersections (Medium, 32 tagged)
https://leetcode.com/problems/interval-list-intersections/

given 2 lists of intervals
firstList: List[List[int]], secondList: List[List[int]]
for both, list[i] = [start_i, end_i]
each list is pairwise disjoint and in sorted order

return the intersection of these 2 interval lists.
"""
from typing import List

# Approach 1
# firstList = [[start_00, end_00], [start_01, end_01], ... , [start_0n, end_0n]]
# secondList = [[start_10, end_10], [start_11, end_11], ... , [start_1m, end_1m]]
# outcome = []
# [1,3], [2,4] -> [2, 3]
# if there's no intersection -> prev_ub < curr_lb
# if curr_lb <= prev_ub: there's intersection
# use a heap like arr to decide which list we should get the next element from

class Solution:
    def interval_intersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        """
        time: O(n+m)
        space: O(1) if arr to store and return is not counted as auxilary space
        :param a:
        :param b:
        :return:
        """
        i = j = 0
        m, n = len(a), len(b)
        arr =[]
        while i < m and j < n:
            lb = max(a[i][0], b[j][0])
            ub = min(a[i][1], b[j][1])
            if lb <= ub:
                arr.append([lb, ub])
            if a[i][1] < b[j][1]:
                i += 1
            else:
                j += 1
        return arr