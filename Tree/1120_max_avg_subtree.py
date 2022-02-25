"""
1120. Maximum Average Subtree
Medium

Given the root of a binary tree, return the maximum average value of a subtree of that tree.
Answers within 10-5 of the actual answer will be accepted.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.
"""
from typing import Optional, List

class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def total_subtree(self, root: Optional[Node]):
        if not root:
            return
        if not (root.left or root.right):
            return root.val, 1, root.val
        else:
            left_sum, left_k, max_left = self.total_subtree(root.left)
            right_sum, right_k, max_right = self.total_subtree(root.right)
            total = left_sum + right_sum + root.val
            root_k = left_k + right_k + 1
            root_avg = total/root_k
            max_avg = max(root_avg, max_left, max_right)
            return total, root_k, max_avg

    def max_avg_subtree(self, root: Optional[Node]) -> float:
        ans = self.total_subtree(root)
        return ans[2]
