"""
426. Convert BST to Sorted Doubly Linked List
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

Medium
"""
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # do inorder traversal
        # prev.right = curr
        # curr.left = prev
        if not root:
            return

        head, prev = None, None

        def dfs(node):
            if not node:
                return
            nonlocal head, prev
            dfs(node.left)
            if not prev:
                head = node
            else:
                prev.right = node
                node.left = prev
            prev = node
            dfs(node.right)

        dfs(root)
        head.left = prev
        prev.right = head
        return head