"""
344. Reverse String (Easy)
https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""
from typing import List

class Solution:
    def reverse_string(self, s: List[str]) -> None:
        def helper(i, j):
            if not i < j:
                return
            s[i], s[j] = s[j], s[i]
            helper(i + 1, j - 1)

        helper(0, len(s) - 1)

    def revserse_iter(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
