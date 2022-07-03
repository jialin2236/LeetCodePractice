"""
124. Binary Tree Maximum Path Sum (H, 23 tagged)
https://leetcode.com/problems/binary-tree-maximum-path-sum/

path: a sequence of nodes where each pari of adjacent nodes in the sequence has an edge connecting them.
a node can only appear in the sequence at most once.

given the root of a binary tree, return the maximum path sum of any non-empty path
"""
from typing import Optional
from TreeNode import TreeNode
import math

# can we use recursion?
# for a node
# max(left_path, 0) + node.val + max(right_path, 0) would be the max sum

#        -10
#    9        20
#          15    7

# 15 - 20 - 7 is the max path

# if we use recursion at a node:
# max(left_path, 0) + node.val + max(right_path, 0) is the max_path of the node, when node is the turning node
# if node act as a path node (an ancestor node as the "turning" node):
# the path length up to this node is: node.val + max(left_path, right_path, 0)

class Solution:
    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        max_sum = int(-math.inf)

        def helper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            # if node as turning point
            l, r = max(helper(node.left), 0), max(helper(node.right), 0)
            path_sum = node.val + l + r
            nonlocal max_sum
            max_sum = max(max_sum, path_sum)
            return node.val + max(l, r)

        helper(root)
        return max_sum
