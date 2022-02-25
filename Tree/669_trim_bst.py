"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high,
trim the tree so that all its elements lies in [low, high].
Trimming the tree should not change the relative structure of the elements that will remain in the tree
(i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# definition of binary search tree: all nodes in left subtree are smaller than the node itself,
# and all nodes in the right subtree are bigger than the node. left subtree and right subtree both
# are BST themselves
class Solution:
    def trim_bst(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if not node:
                return
            elif node.val < low:
                return trim(node.right)
            elif node.val > high:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

    def trim_bst0(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return
        else:
            if root.val < low:
                root = self.trim_bst0(root.right, low, high)
            if root.val > high:
                root = self.trim_bst0(root.left, low, high)
            else:
                root.left = self.trim_bst0(root.left, low, high)
                root.right = self.trim_bst0(root.right, low, high)
            return root