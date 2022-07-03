"""
28. implement strStr()
"""

"""
given strings pattern and txt, return first index in txt where pattern is found in txt
(finding substring pattern in txt)
"""

class Solution:
    def strStr_naive(self, p: str, s: str) -> int:
        """
        time: O(m*n)
        space: O(1)
        :param p:
        :param s:
        :return:
        """
        m, n = len(s), len(p)
        for i in range(m - n):
            if s[i:i + n] == p:
                return i
        return -1

    def kmp_matching(self, p: str, s: str) -> int:
        """
        time: O(m)
        space: O(n)
        :param p:
        :param s:
        :return:
        """
        def get_lps(pattern):
            lps = [0 for _ in range(len(pattern))]
            i, j = 1, 0
            while i < len(pattern):
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = lps[j-1]
                    else:
                        i += 1
            return lps

        m, n = len(s), len(p)
        i, j = 0, 0
        lps = get_lps(p)
        while i < m:
            if s[i] == p[j]:
                i += 1
                j += 1
            if j == n:
                return i - n
            if i < m and s[i] != p[j]:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
        return -1