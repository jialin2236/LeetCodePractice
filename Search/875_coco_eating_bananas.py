"""
875. Koko Eating Bananas (Medium)
https://leetcode.com/problems/koko-eating-bananas/

1. n piles of bananas, given piles: List[int], the i-th piles has piles[i] bananas
2. the guards have gone and will be back in h hours
3. each hour, she chooses one pile of bananas and eats k from that pile
4. if the pile has less than k, she won't eat more during the hour

find the minimum integer k such that Koko can eat all the bananas within h hours

condition: h >= len(piles) -> always feasible
"""
from typing import List

# example
# piles = [3,6,7,11], h = 8
# output: 4

# min speed = 1 -> eating 1 bananas per hour, it'll take sum(piles) hours to finish
# max speed = max(piles) -> guaranteed eating one pile per hour, it'll take len(piles) hours to finish
# to finish eating all banans in h hours
# each pile takes ceil(pile//k) -> (pile + 1) // k hours, if adding up <= h -> feasible

class Solution:
    def min_speed(self, piles: List[int], h: int) -> int:
        def quick_enough(k: int) -> bool:
            hours = 0
            for pile in piles:
                hours += (pile//k + 1)
                if hours > h: return False
            return True

        lb, ub = 1, max(piles)
        while lb < ub:
            mid = lb + (ub - lb) // 2
            if quick_enough(mid):
                # mid is quick enough, we can try to slow down and explore lower speed
                # since mid - 1 may not be quick enough, we keep mid in our search space
                ub = mid
            else:
                # mid is not quick enough, we need to increase speed
                # since mid is not feasible, we exclude it from our search space
                lb = mid + 1
        return lb