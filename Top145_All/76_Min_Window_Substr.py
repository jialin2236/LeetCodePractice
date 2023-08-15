"""
76. Minimum Window Substring
"""
from collections import Counter, deque

# input s: str, t: str
# output str
# the minimum substring in s that has every chars in t, including duplicates

class Solution: 
    def minWindow(self, s: str, t: str) -> str: 
        target = Counter(t)
        # curr - the counter for current substring window
        # matched - number of characters with sufficient occurrence in current window
        curr, stack, matched = Counter(), deque(), 0
        min_len, res = float("inf"), None
        i = 0
        for j in range(len(s)): 
            if s[j] in target: 
                curr[s[j]] += 1
                stack.append(j)
                if curr[s[j]] == target[s[j]]: 
                    matched += 1
            if not curr:
                i += 1
            while matched == len(target):
                if j - i + 1 < min_len:
                    min_len, res = j - 1 + 1, s[i:j+1]
                k = stack.popleft()
                curr[s[k]] -= 1
                if curr[s[k]] < target[s[k]]: 
                    matched -= 1
                i = stack[0]
        return res if res else ''