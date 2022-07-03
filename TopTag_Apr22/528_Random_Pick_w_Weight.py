"""
528. Random Pick with Weights (M, 137)
"""

# what we know
# given an array w: List[int] (positive) w[i] - weight of ith index
# implement function pickIndex(), randomly picks an index in the range [0, w.length - 1] and returns it
# uniformly (prob[i] = w[i] / sum(w))

# total = sum(w)
# r = random.randint(0, total - 1)
# use cumulative sum, traverse through array, if cumulative sum < r -> continue
# else break -> return i

from typing import List
import random

class Solution:
    def __init__(self, w: List[int]):
        """
        we use binary search on the cumulative weights of the w array
        time: O(logN) every time pickIndex is called
        space: O(N) for the cumulative sum array made
        :param w:
        """
        self.prefix_sums = []
        prefix_sum = 0
        for wi in w:
            prefix_sum += wi
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self):
        r = random.random() * self.total
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = (low + high) // 2
            if r > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low