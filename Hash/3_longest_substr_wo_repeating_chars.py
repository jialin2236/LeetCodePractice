"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

tag: hashmap, sliding window
"""

class Solution:
    def lengthOflongestSubstr(self, s: str) -> int:
        n_chars = {}
        n = len(s)
        i = 0
        ans = 0
        for j in range(n):
            if s[j] in n_chars and n_chars[s[j]] > i:
                i = n_chars[s[j]] + 1
            ans = max(ans, j-i+1)
            n_chars[s[j]] = j
        return ans