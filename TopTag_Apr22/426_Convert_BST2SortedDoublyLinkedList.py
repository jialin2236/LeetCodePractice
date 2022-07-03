"""
426. Convert Binary Search Tree to Sorted Doubly Linked List (M, 72)
"""
from Tree import trees
from typing import Optional

# into a sorted circular doubly-linked list, in place
# left pointer of tree node should point to predecessor
# right pointer to its successor
# return pointer to the smallest element of the linked list

class Solution:
    def tree2doubly_linkedlist(self, root: Optional[trees.TreeNode]) -> Optional[trees.TreeNode]:
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