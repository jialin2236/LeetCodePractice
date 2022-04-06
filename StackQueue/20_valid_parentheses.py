"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


class Solution(object):
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2:
            return False
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for si in s:
            if si in pairs:
                stack.append(si)
            else:
                if not stack:
                    return False
                tail = stack.pop()
                if pairs[tail] != si:
                    return False
        return stack == []



