"""
986. Interval List Intersections (Medium, 32 tagged)
https://leetcode.com/problems/interval-list-intersections/

given 2 lists of closed intervals. Each list is pairwise disjoint and in sorted order.

return the intersection of these two interval lists.
"""
from typing import List

# example
# a = [[0,2], [5,10], [13,23], [24,25]]
# b = [[1,5], [8,12], [15,24], [25,26]]
# -> [[1,2], [5,5], [8,10], [15,23], [24, 24], [25, 25]]

# loop through both lists
# when we reach the end of one list, since the other list is disjoint, we finish the task
# at each iteration, combine the intervals from a and b
# ex: step 0, combine [0,2] and [1,5] -> [1,2]
# since the intersection with a larger upper bound, could still intersect with the lower bound of the next interval
# in the other list
# ex: [1,5] from b[0], ub = 5, intersects with lb of a[1]
# can we only move the pointer for the list with the lower upper bound
# a[i][1] < b[j][1]: i += 1 else j += 1
# if ub is the same, it doesn't matter
# To summarize it:
# i < m and j < n:
# new_intersection = [max(a_lb, b_lb), min(a_ub, b_ub)]
# if a_ub < b_ub: j+= 1 else: i+=1

class Solution:
    def interval_intersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        """
        time: O(m + n)
        space: O(m + n)
        :param a:
        :param b:
        :return:
        """
        i, j = 0, 0
        ans = []
        while i < len(a) and j < len(b):
            # determine new intersection to add to answer
            # if no intersection: [1,5] [7,9]
            lb, ub = max(a[i][0], b[j][0]), min(a[i][1], b[j][1])
            if lb <= ub:
                intersection = [lb, ub]
                ans.append(intersection)
            if a[i][1] < b[j][1]:
                i += 1
            else:
                j += 1
        return ans