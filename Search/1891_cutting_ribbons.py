"""
1891. Cutting Ribbons (Medium)
https://leetcode.com/problems/cutting-ribbons/

You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
- Keep the ribbon of length 4,
- Cut it into one ribbon of length 3 and one ribbon of length 1,
- Cut it into two ribbons of length 2,
- Cut it into one ribbon of length 2 and two ribbons of length 1, or
- Cut it into four ribbons of length 1.

Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you cannot obtain k ribbons of the same length.
"""
from typing import List


# first we can consider a simpler question: is it feasible to obtain k ribbons of length l?
def feasible_ribbon(ribbons: List[int], k: int, l: int) -> bool:
    total = 0
    for ribbon in ribbons:
        # if each cut ribbon should be of length l, how many ribbons the current ribbon can make?
        total += ribbon // l
    return total >= k

# option 1: we can use a linear search to find the maximum value of l, where feasible_ribbon is still True
# options 2: we can use binary search to find the maximum feasible value of l
#            minimum feasible value of l = min(1, max(ribbons)//k)
#            maximum feasible value of l = min(max(ribbons), sum(ribbons)//k)
#           -> the lower bound of our binary search is min(1, max(ribbons)//k),
#                  upper bound is min(max(ribbons), sum(ribbons)//k)


def max_length(ribbons: List[int], k: int) -> int:
    total = sum(ribbons)
    if total < k:
        # if the total length of all ribbon is smaller than k -> we cannot obtain k ribbons, even with length 1
        return 0
    # if ribbons = [1,1,1,1], k = 2 -> total // k = 2 that's not feasible, ub should be max(ribbons) = 1
    #                               -> max(ribbons) // k = 0 that's meaningless, lb should be 1
    lb = max(1, max(ribbons)//k)
    ub = min(max(ribbons), total//k)
    while lb < ub:
        # rounding up mid to avoid infinite loop when lb = ub - 1
        mid = (lb + ub + 1) // 2
        if feasible_ribbon(ribbons, k, mid):
            # mid is feasible -> explore larger length options
            # have to set lb to mid, since mid + 1 may not be feasible
            lb = mid
        else:
            # we know for sure mid is not feasible (too large), explore smaller options
            # since mid could be discarded, set ub to mid - 1
            ub = mid - 1
    return lb