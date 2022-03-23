"""
700. Search in a Binary Search Tree (easy)
https://leetcode.com/problems/search-in-a-binary-search-tree/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
If such a node does not exist, return null.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def search_bst(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        return self.search_bst(root.left, val) if val < root.val else self.search_bst(root.right, val)
