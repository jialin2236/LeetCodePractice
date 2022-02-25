"""
791. Custom Sort String
Medium

You are given two strings order and s.
All the words of order are unique and were sorted in some custom order previously.

Permute the characters of s so that they match the order that order was sorted.
More specifically, if a character x occurs before a character y in order,
then x should occur before y in the permuted string.

Return any permutation of s that satisfies this property.
"""

"""
thoughts
question: 
1. are all characters in order present in s? 
2. are all characters in s present in order? 
"""
from collections import Counter


class Solution:
    def custom_sort_string(self, s: str, order: str) -> str:
        freq = Counter(s)
        ans = []
        for ch in order:
            if ch in freq:
                ans.append(ch * freq[ch])
                freq.pop(ch)
        for ch in freq:
            ans.append(ch * freq[ch])
        return ''.join(ans)
