"""
10. Regular Expression Matching
"""

# input s: str, p: str
# problem/task implement regular expression with support for '.' and '*'
# '.' matches any single character
# '*' zero or more occurrences of the preceding element
# ab*c matches "ac", "abc", "abbc", "abbbc", and so on.

# 'a.' -> exact match of a, and anything in the next index
# 'a*' -> 1. exact match of a + multiple a 'aaaaa' -> replicate previous char as many as needed
#         2. skipping a char, matching 1 a 'a'  -> act as . skip to next
#         3. matching zero of the preceding element, '' -> remove previous occurence of a


class Solution:
    def isMatch_topdown(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= m and j >= n:
                return True
            if j >= n:
                return False

            match = i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j + 1] == '*':
                cache[(i, j)] = dfs(i, j + 2) or (dfs(i + 1, j) and match)
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)

    def isMatch_dp(self, s: str, p: str):
        if p: return not s

        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        # empty strings
        dp[0][0] = True

        # first row
        # dp[0][j] = True if j == '*' and previously eliminated all
        for j in range(2, n + 1):
            dp[0][j] = dp[0][j - 2] and p[j] == '*'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # 1. not to use any occurrence of prev in p
                    # 2. s[i-1] == p[j-2] or p[j-2] == '.', dp[i-1][j] (????????)
                    # 'ba' 'a*'
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
        return dp[m][n]