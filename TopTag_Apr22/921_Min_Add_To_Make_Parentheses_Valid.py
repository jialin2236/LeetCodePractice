"""
921. Minimum Add to Make Parentheses Valid (M, 106)
"""

# Approach
# can we keep n_open, n_close, n_add??
# while traversing s
# if s[i] == "(" -> n_open += 1 unmatched_open += 1
# if s[i] == ")" -> unmatched_open -= 1 if unmatched_open > 0, else n_add += 1

# "((())" unmatched_open = 1 -> 2 -> 3 -> 2 -> 1
# "(((" unmatched_open = 1 -> 2 -> 3
# "))((()" unmatched_open = 0 -> 0 -> 1 -> 2 -> 3 -> 2 n_add = 1 -> 2
# "((()()(("

class Solution:
    def min_add2make_valid(self, s: str) -> int:
        open, close = 0, 0
        for char in s:
            if char == '(':
                open += 1
            if char == ')':
                if open:
                    open -= 1
                else:
                    close += 1
        return open + close