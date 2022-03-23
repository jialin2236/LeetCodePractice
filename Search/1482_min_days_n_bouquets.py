"""
1482. Minimum Number of Days to Make m Bouquets (Medium)
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

1. bloomDay: List[int], m: int, k: int
2. make m bouquets using k adjacent flowers
3. garden consists of n flowers, i-th flower will bloom in the bloomDay[i], can be used in exactly one bouquet

return minimum number of days you need to wait to make m bouquets. if not possible, return -1
"""
from typing import List

# example
# bloomDay = [1,10,3,10,2], m = 3, k = 1 -> 3
# [x,_,_,_,_] -> [x,_,_,_,x] -> [x,_,x,_,x] -> 3 bouquets in 3 days
# bloomDay = [1,10,3,10,2], m = 3, k = 2 -> -1
# to make 3 bouquets each with 2 flowers, we need 6 flowers, there are only 5 in the garden

# lb = 1 if enough flowers bloom on the first day
# ub = max(bloomDay) if we need all flowers in the garden to bloom, and bloomDay differs
# if len(bloomDay) < m * k -> not feasible


class Solution:
    def min_days(self, bloomDay: List[int], k: int, m: int) -> int:
        flowers_needed = m * k
        if len(bloomDay) < flowers_needed:
            return -1

        def feasible(days: int) -> bool:
            n_flowers = 0
            for flower in bloomDay:
                n_flowers += 1 if flower <= days else 0
            return n_flowers >= flowers_needed

        lb, ub = 1, max(bloomDay)
        while lb < ub:
            mid = lb + (ub - lb) // 2
            if feasible(mid):
                ub = mid
            else:
                lb = mid + 1
        return lb