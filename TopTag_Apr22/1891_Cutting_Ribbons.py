"""
1891. Cutting Ribbons (M, 24)
"""

from typing import List

# given ribbons: List[int] represents length of different ribbons
#       k: int
# we need to cut available ribbons to achieve k ribbons of the same length
# find the maximum length of these ribbons
# 0 if it's not feasible

class Solution:
    def max_length(self, ribbons: List[int], k: int) -> int:
        """
        time: O(Nlog(max_length)) or O(Nlog(total_length//k))
        space: O(1)
        :param ribbons:
        :param k:
        :return:
        """
        # if the total length of all ribbons is less than k
        # we cannot obtain k ribbons of the same length, even if we cut them into 1 unit length
        if sum(ribbons) < k:
            return 0

        # given a proposed per ribbon length
        # we can determine if the proposed length is feasible, given the list of ribbon lengths we have
        def feasible(x):
            total = 0
            for r in ribbons:
                # we can get r // x ribbons out of ribbon r if we want length of x
                total += r // x
                if total >= k:
                    # if we get at least k ribbons already
                    return True
            return False

        # we can simply cut the longest ribbon into k pieces, if it's long enough
        # if not, we know we can at least get unit length of 1 ribbons (otherwise sum(ribbons) would be < k)
        lo = max(max(ribbons) // k, 1)
        # if all ribbon lengths are equal enough, and we won't need to toss out any ribbon
        # -> unit length = sum(ribbons) // k
        # but if k == 1, then we can just take the longest original ribbon, uncut
        hi = min(max(ribbons), sum(ribbons) // k)
        while lo < hi:
            mid = hi - (lo + hi) // 2
            if feasible(mid):
                # mid is feasible, explore higher value
                lo = mid
            else:
                # mid is not feasible, explore lower value, knowing mid is not a possible answer
                hi = mid - 1
        return lo