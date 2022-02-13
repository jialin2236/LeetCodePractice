"""
Given the root of a binary tree, invert the tree,
and return its root.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        return root

    def inverTree_i(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = [root]
        while queue:
            curr = queue.pop(0)
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
