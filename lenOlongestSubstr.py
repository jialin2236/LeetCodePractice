class Solution(object):
    def lengthOfLongestSubstringO2n(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_l = 0
        lookup = {}
        for j in range(len(s)):
            if s[j] in lookup.keys():
                max_l = max(max_l, j - lookup[s[j]])
            lookup[s[j]] = j
        return max_l

    def lengthOfLongestSubstringOn(self, s):
        max_l = 0
        for i in range(len(s)):
            if i + max_l <= len(s) - 1:
                sub_i = s[i:i+1]
                for j in range(i+2, len(s)+1):
                    sub_s = s[i:j]
                    incr_s = len([c for c in sub_s if c not in sub_i])
                    if incr_s == 0:
                        if len(sub_i) > max_l:
                            max_l = len(sub_i)
                        break
                    else:
                        sub_i = sub_s
            else:
                pass
        return max_l

