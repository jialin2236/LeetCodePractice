"""
301. Remove Invalid Parentheses (Hard, 35 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/remove-invalid-parentheses/

Given a string s that contains parentheses and letters,
remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.
"""
from typing import List
from collections import defaultdict

# key words: return all possible results, in any order
# since we don't know the if a removal would lead to valid final string, we'd need to explore all possibilities
# use backtracking


class Solution:
    def remove_invalid_parentheses(self, s: str) -> List[str]:
        n = len(s)
        ans = defaultdict(list)

        def backtrack(idx, path, n_open, n_rmv):
            if idx == n and n_open == 0:
                ans[n_rmv].append(path)
                return
            if s[idx] not in ["(", ")"]:
                backtrack(idx + 1, path + s[idx], n_open, n_rmv)
            else:
                backtrack(idx + 1, path, n_open, n_rmv + 1)
                if s[idx] == "(":
                    backtrack(idx + 1, path + s[idx], n_open + 1, n_rmv)
                elif n_open > 0:
                    backtrack(idx + 1, path + s[idx], n_open - 1, n_rmv)

        backtrack(0, '', 0, 0)
        min_rmv = min(ans.keys())
        return ans[min_rmv]
