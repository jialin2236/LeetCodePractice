"""
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Medium
"""
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def diameter_of_binary_tree(self, root: Optional[Node]) -> int:
        diameter = 0

        def depth(node: Optional[Node]) -> int:
            if not node:
                return 0
            nonlocal diameter
            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        depth(root)
        return diameter