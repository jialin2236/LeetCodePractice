"""
1026. Maximum Difference Between Node and Ancestor (Medium)
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b
where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""
from trees import TreeNode
from typing import Optional


# we will need to traverse the entire tree in order to find out the answer
# since all we know is the tree is a binary tree, and there is no other information about it
# we need to find out
# LCA relationship
# min_value of the subtree, max_value of the subtree
# max_diff along the process

class Solution:
    def max_ancestor_diff(self, root: Optional[TreeNode]) -> int:
        max_diff = 0

        def diff(node: Optional[TreeNode], max_val: int, min_val: int):
            if not node:
                return
            node_diff = max(abs(node.val - max_val), abs(node.val - min_val))
            nonlocal max_diff
            if node_diff > max_diff:
                max_diff = node_diff
            new_max, new_min = max(max_val, node.val), min(min_val, node.val)
            diff(node.left, new_max, new_min)
            diff(node.right, new_max, new_min)

        diff(root, root.val, root.val)
        return max_diff