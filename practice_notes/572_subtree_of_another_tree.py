"""
Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
The tree tree could also be considered as a subtree of itself.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isIdentical(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot:
            if root.val == subRoot.val:
                left = self.isIdentical(root.left, subRoot.left)
                right = self.isIdentical(root.right, subRoot.right)
                return left and right
        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isIdentical(root, subRoot):
            return True

        if self.isSubtree(root.left, subRoot):
            return True

        if self.isSubtree(root.right, subRoot):
            return True

        return False