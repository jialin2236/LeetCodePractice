"""
173. BST Iterator (M, 43)
"""

# implement BSTIterator class with root node
# an iterator over the in-order traversal of a BST
# has_next: bool if the iterator has a next number
# next: int return the next number

# requirement
# time complexity to be O(1) per call for next()
# space complexity to be O(h)

from Tree import trees
from typing import Optional
from collections import deque

class BSTIterator:
    """
    time: each node will be pushed into, and popped exactly one time in the process
          -> N * O(1) -> for N next calls, each call average O(1)
    space: O(h)
    """
    def __init__(self, root: Optional[trees.TreeNode]):
        self.stack = deque()
        self._left_branch(root)

    def _left_branch(self, node: Optional[trees.TreeNode]):
        curr = node
        while curr:
            self.stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        curr = self.stack.pop()
        self._left_branch(curr)
        return curr.val

    def has_next(self) -> bool:
        return len(self.stack) > 0