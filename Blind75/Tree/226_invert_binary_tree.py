"""
226. invert binary tree (E, 5 tagged)
https://leetcode.com/problems/invert-binary-tree/

given root of a binary tree, invert the tree and return its root
"""
from typing import Optional
from TreeNode import TreeNode

# use recursion
# invert leaf node first, then resurse up the tree all the way to root

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            # if root is Null, return itself
            return root
        l, r = self.invert_tree(root.left), self.invert_tree(root.right)
        root.left, root.right = r, l
        return root
    