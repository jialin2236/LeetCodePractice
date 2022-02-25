"""
438. Find All Anagrams in a String
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from typing import List
from collections import Counter


class Solution:
    def find_anagrams(self, s: str, p: str) -> List[int]:
        s_counter, p_counter = Counter(), Counter(p)
        ns, np = len(s), len(p)
        ans = []
        left = right = 0
        while left < ns - np:
            while right - left + 1 <= np:
                s_counter[s[right]] += 1
                right += 1
            if s_counter == p_counter:
                ans.append(left)
            s_counter[s[left]] -= 1
            if not s_counter[s[left]]:
                del s_counter[s[left]]
            left += 1
        return ans
