"""
Given a string s,
reverse the order of characters in each word within a sentence while still preserving
whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Input: s = "God Ding"
Output: "doG gniD"
"""

class Solution:
    def reverse_w(self, word: str, i: int, j: int) -> None:
        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1

    def reverse_w_str(self, s: str) -> str:
        si, ans = "", ""
        for j in range(len(s)):
            if s[j] != " ":
                si += s[j]
            else:
                self.reverse_w(si, 0, len(si)-1)
                ans += (si + " ")
                si = ""
        return ans

    def reverse_w_str1(self, s: str) -> None:
        i = j = 0
        while j < len(s) - 1:
            if s[j + 1] != " ":
                j += 1
            else:
                self.reverse_w(s, i, j)
                j += 2
                i = j
        self.reverse_w(s, i, j)

