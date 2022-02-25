"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/

Easy

Given the root of a binary tree, return the inorder traversal of the
node's value.
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if node:
                nonlocal ans
                dfs(node.left)
                ans.append(node.val)
                dfs(node.right)

        dfs(root)
        return ans
