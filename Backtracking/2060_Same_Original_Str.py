"""
2060. Check if an Original String Exists Given Two Encoded Strings (Hard, 11 tagged)
https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

a string with lowercase letters could be encoded as:
1. split string into a sequence of non-empty substrings
2. randomly pick some substrings and replace it with the length
3. concat the seq
"""

# example
# 'abcdefghijklmnop' -> 'a,b,12,1,p'
# s1 = 'l123e', s2 = '44'

# Approach
# use backtracking with length from s1 and length from s2
# i = pointer for s1
# j = pointer for s2
# s_idx1 = pointer for imaginary original string when using s1
# s_idx2 = pointer for imaginary original string when using s2

class Solution:
    def equal_encode(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        # determine if there's difference in length in original s s1 and s2 is pointing to
        def str2num(s):
            # return possible length extension when s1/s2 encounters digits
            ans = {int(s)}
            for i in range(1,len(s)):
                ans |= {x + y for x in str2num(s[:i]) for y in str2num(s[i:])}
            return ans

        def probe(i, j, diff):
            if i == m and j == n:
                return diff == 0
            if i < m and s1[i].isdigit():
                ii = i
                while ii < m and s1[ii].isdigit(): ii += 1
                for x in str2num(s1[i:ii+1]):
                    return probe(ii, j, diff - x)
            elif j < n and s2[j].isdigit():
                jj = j
                while jj < n and s2[jj].isdigit(): jj += 1
                for y in str2num(s2[j:jj+1]):
                    return probe(i, jj, diff - y)
            elif diff == 0:
                if i < m and j < n and s1[i] == s2[j]:
                    return probe(i + 1, j + 1, 0)
            elif diff > 0:
                if i < m:
                    return probe(i + 1, j, diff - 1)
            else:
                if j < n:
                    return probe(i, j + 1, diff + 1)
            return False

        return probe(0, 0, 0)