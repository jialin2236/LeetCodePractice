"""
236. Lowest Common Ancestor of a Binary Tree
Medium


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
from typing import Optional, Dict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Idea
# Traverse the tree till finds nodes that are parents of p and q, if the 2 nodes are not the same
# recursively call function on 2 parents until 2 parents converge to the same node
class Solution:
    def find_parent(self, root: TreeNode, node: TreeNode) -> Optional[TreeNode]:
        if not root:
            return
        left, right = root.left, root.right
        if left == node or right == node:
            return root
        LS = self.find_parent(root.left, node)
        if LS:
            return LS
        RS = self.find_parent(root.right, node)
        if RS:
            return RS

    def load_parent(self, root: TreeNode, p: TreeNode, q:TreeNode) -> Dict:
        queue = [root]
        parents = {root: None}
        while queue and (p not in parents or q not in parents):
            node = queue.pop()
            if node.left:
                left = node.left
                parents[left] = node
                queue.append(left)
            if node.right:
                right = node.right
                parents[right] = node
                queue.append(right)
        return parents

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = self.load_parent(root, p, q)
        p_stack = set()
        while p:
            p_stack.add(p)
            p = parents[p]
        while q not in p_stack:
            q = parents[q]
        return q
