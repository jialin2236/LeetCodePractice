"""
680. Valid Palindrome II
Easy

Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

class Solution:
    def valid_palindrome_ii(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        mod = 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif s[i] == s[j - 1] and mod == 0:
                i += 1
                j -= 2
                mod += 1
            elif s[i+1] == s[j] and mod == 0:
                i += 2
                j -= 1
                mod += 1
            else:
                return False
        return True

    def valid_palindrome_util(self, s: str, start: int, end: int) -> bool:
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def valid_palindrome_ii0(self, s: str):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.valid_palindrome_util(s, i, j-1) or self.valid_palindrome_util(s, i + 1, j)
        return True