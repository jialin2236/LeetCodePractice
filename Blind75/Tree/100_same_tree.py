"""
100. same tree (easy, 0 tagged)
https://leetcode.com/problems/same-tree/

given roots of two binary tree p and q, check if they are the same or not
"""
from typing import Optional
from TreeNode import TreeNode

# use recursion for checking

class Solution:
    def same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not (p or q):
            # both are None
            return True
        if not (p and q):
            # only one of them is None
            return False
        if p.val != q.val:
            return False
        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)
