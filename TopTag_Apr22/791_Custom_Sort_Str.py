"""
791. Custom Sort String (M, 63)
"""
from collections import Counter

# given order: str, s: str
# permute s (re-arrange) to match the order that order was sorted. if a character in s is not in order, it can be placed
# anywhere in the returned string

# use counter

class Solution:
    def custom_sort_string(self, order: str, s: str) -> str:
        """
        time: O(m + n)
        space: O(n)
        :param order:
        :param s:
        :return:
        """
        cnt_s = Counter(s)
        ans = ''
        for c in order:
            if c in cnt_s:
                ans += c * cnt_s[c]
                del cnt_s[c]
        for c in cnt_s:
            ans += c * cnt_s[c]
        return ans