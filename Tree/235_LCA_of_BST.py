"""
235. Lowest Common Ancestor of a Binary Search Tree (easy)
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
"""

# we can take advantage of the property of a bst
# if both nodes belong to the same subtree of a node, move down to that subtree
# otherwise, the node is the LCA of the two nodes, since we traverse down the root node
from trees import TreeNode


class Solution:
    def LCA(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pv, qv = p.val, q.val
        node = root
        while node:
            if pv < node.val and qv < node.val:
                node = node.left
            elif pv > node.val and qv > node.val:
                node = node.right
            else:
                return node

