"""
104. Max depth of a binary tree (easy, 0 tagged)
https://leetcode.com/problems/maximum-depth-of-binary-tree/

given root of a binary tree, return its maximum depth
(number of nodes along the longest path from the root node down to the farthest leaf node
"""
from typing import Optional
from TreeNode import TreeNode

# use recursion with a second variable of depth
# have a global variable of max_depth, and compare as we go

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0

        def helper(node: Optional[TreeNode], depth):
            if not node:
                return
            depth += 1
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            helper(node.left, depth)
            helper(node.right, depth)

        helper(root, 0)
        return max_depth
