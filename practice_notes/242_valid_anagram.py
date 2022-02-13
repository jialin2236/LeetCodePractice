"""
Given two strings s and t, return true if t is an anagram of s,
and false otherwise.
"""

"""
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
"""
from collections import OrderedDict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = OrderedDict()
        for i in s:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        for j in t:
            if j not in counter:
                return False
            counter[j] -= 1
            if counter[j] == 0:
                del counter[j]
        return len(counter) == 0

    def isAnagram_s(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_arr = [si for si in s]
        t_arr = [ti for ti in t]
        return s_arr.sort() == t_arr.sort()
