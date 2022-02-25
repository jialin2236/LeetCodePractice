"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""
from typing import List


class Solution:
    def gen_parentheses(self, n: int) -> List[str]:
        len_s = 2 * n
        ans = []

        def gen_combination(combo, open, close):
            if len(combo) == len_s:
                ans.append(''.join(combo))
                return

            if open < n:
                combo.append('(')
                gen_combination(combo, open + 1, close)
                combo.pop()
            if close < open:
                combo.append(')')
                gen_combination(combo, open, close + 1)
                combo.pop()
            return ans

        return gen_combination([], 0, 0)