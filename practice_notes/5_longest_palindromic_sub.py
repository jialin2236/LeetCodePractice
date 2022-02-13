class Solution:
    def longestPalindromDP(self, s: str) -> str:
        max_len, n, max_start = 0, len(s), 0
        dp = [[0] * n for _ in range(n)]
        # bottom up
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = (i == j) or (j == i + 1) or (dp[i+1][j-1])
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    max_start = i
        return s[max_start:max_len + 1]

    def longestPalindromRp(self, s):
        lenS = len(s)
        if lenS <= 1:
            return s
        minStart, maxLen, i = 0, 1, 0
        while i < lenS:
            if lenS - i <= maxLen / 2:
                break
            j, k = i, i
            while k < lenS - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while k < lenS - 1 and j and s[k + 1] == s[j - 1]:
                k, j = k + 1, j - 1
            if k - j + 1 > maxLen:
                minStart, maxLen = j, k - j + 1
        return s[minStart: minStart + maxLen]

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self, s):
        n = len(s)
        max_len = 0
        left = right = 0
        for i in range(n):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            max_len1 = max(len1, len2)
            if max_len1 > max_len:
                max_len = max_len1
                left = i - (max_len-1)//2
                right = left + max_len
        return s[left:right]


if __name__ == '__main__':
    solve = Solution()
    s1 = 'ccc'
    print(solve.longestPalindrome(s1))
