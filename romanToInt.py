class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = lookup[s[0]]
        for i in range(len(s)-1):
            n0 = lookup[s[i]]
            n1 = lookup[s[i+1]]
            if n0 >= n1:
                n_ = n1
            else:
                n_ = -2*n0 + n1
            n += n_
        return n