"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n,
return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
"""
"""
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

[1,0,0,0]
"""
from typing import List


class Solution:
    def fitFlowers(self, f: List[int], n: int) -> bool:
        i, count = 0, 0
        length = len(f)
        while i < length:
            if f[i] == 0 and (f[i - 1] == 0 or i == 0) and (f[i + 1] == 0 or i == length - 1):
                f[i] = 1
            count += 1
            if count >= n:
                return True
            i += 1
        return False
