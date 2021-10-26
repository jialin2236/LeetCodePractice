class Solution(object):
    def centerxpand(self, s, li, ri):
        while li >= 0 and ri < len(s) and s[li] == s[ri]:
            li -= 1
            ri += 1
        return ri - li - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = right = 0
        for i in range(len(s)):
            l1 = self.centerxpand(s, i, i)
            l2 = self.centerxpand(s, i, i+1)
            l = max(l1,l2)
            if l > right - left:
                left = int(i - (l-1)/2)
                right = int(i + l/2)
            result = s[left:right+1]
        return result

