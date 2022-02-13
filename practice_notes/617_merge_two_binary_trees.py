"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def mergeTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        if not root1:
            return root2
        if not root2:
            return root1
        if root1 and root2:
            mval = root1.val + root2.val
            node = TreeNode(mval)
            node.left = self.mergeTree(root1.left, root2.left)
            node.right = self.mergeTree(root2.right, root2.right)
            return node
