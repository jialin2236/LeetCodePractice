"""
301. Remove Invalid Parentheses (H, 44)
"""
from typing import List
from collections import defaultdict
from functools import lru_cache
# given a string s with letters and parentheses
# return list of strings that are valid parentheses strings with minimum removal

# use backtracking?
# with memoization

class Solution:
    def remove_invalid_par_optimal(self, s: str) -> List[str]:
        """
        time: O(2^N)
        space: O(N)
        :param s:
        :return:
        """
        extra_open, extra_close = 0, 0
        n, res = len(s), set()

        for c in s:
                if c == '(':
                    extra_open += 1
                elif c == ')':
                    if not extra_open:
                        extra_close += 1
                    else:
                        extra_open -= 1

        @lru_cache(None)
        def helper(i, n_open, n_close, open_2rmv, close_2rmv, path):
            if i == n:
                if not (open_2rmv or close_2rmv):
                    res.add(path)
                return
            else:
                # condition where we could remove s[i]
                if (s[i] == '(' and open_2rmv > 0) or (s[i] == ')' and close_2rmv > 0):
                    helper(i + 1, n_open, n_close, open_2rmv - (s[i] == '('), close_2rmv - (s[i] == ')'), path)
                # condition where we could include s[i]
                if s[i] not in '()':
                    helper(i + 1, n_open, n_close, open_2rmv, close_2rmv, path + s[i])
                elif s[i] == '(':
                    helper(i + 1, n_open + 1, n_close, open_2rmv, close_2rmv, path + s[i])
                elif s[i] == ')' and n_open > n_close:
                    # for ')', only add when where's additional opens seen for it to match to
                    helper(i + 1, n_open, n_close + 1, open_2rmv, close_2rmv, path + s[i])

        helper(0, 0, 0, extra_open, extra_close, '')
        return list(res)

    def remove_invalid_parentheses(self, s: str) -> List[str]:
        """
        time: O(2^N)
        space: O(N)
        :param s:
        :return:
        """
        n = len(s)
        memo = defaultdict(set)
        max_len = 0

        @lru_cache(None)
        def helper(i: int, balance: int, path: str):
            if i == n:
                if balance == 0:
                    nonlocal max_len
                    if len(path) >= max_len:
                        memo[max_len].add(path)
                        max_len = len(path)
                return
            # s[i] is letter
            if s[i] not in '()':
                helper(i + 1, balance, path + s[i])
            # s[i] is parentheses
            else:
                # ignoring it is always an option
                helper(i + 1, balance, path)
                # only when
                # 1. s[i] is ')' and we have more open than close
                # 2. s[i] is '('
                # where we can include the parentheses and still might come to a valid string
                if (s[i] == ')' and balance > 0) or (s[i] == '('):
                    if s[i] == ')':
                        helper(i + 1, balance - 1, path + s[i])
                    else:
                        helper(i + 1, balance + 1, path + s[i])

        helper(0, 0, '')
        return list(memo[max_len])