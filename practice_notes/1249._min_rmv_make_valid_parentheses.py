"""
1249. Minimum Remove to Make Valid Parentheses
Medium

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

(((aabbcc)))
"""


class Solution:
    def make_valid_parentheses(self, s: str) -> str:
        stack = []
        rmv = set()
        for i in range(len(s)):
            if s[i].isalpha():
                continue
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    rmv.add(i)
                else:
                    stack.pop()
        if stack:
            rmv = rmv.union(set(stack))
        ans = []
        for j in range(len(s)):
            if j not in rmv:
                ans.append(s[j])
        return ''.join(s)

    def make_valid_parentheses2(self, s: str) -> str:
        num_open = unmatched_open = 0
        filtered = []
        for c in s:
            if c == '(':
                num_open += 1
                unmatched_open += 1
            if c == ')':
                if unmatched_open == 0:
                    continue
                else:
                    unmatched_open -= 1
            filtered.append(c)
        ans = []
        matched_open = num_open - unmatched_open
        for c in filtered:
            if c == '(':
                if matched_open == 0:
                    continue
                matched_open -= 1
            ans.append(c)
        return ''.join(ans)