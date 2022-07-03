"""
1047. Remove All Adjacent Duplicates In String
"""
from collections import deque

# choose 2 adjacent and identical characters and remove them

class Solution:
    def remove_duplicates(self, s: str) -> str:
        stack = deque()
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)