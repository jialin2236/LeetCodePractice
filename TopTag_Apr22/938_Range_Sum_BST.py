"""
938. Range Sum of BST (E, 162)
"""

# what we know?
# input - root: TreeNode
# tree is a bst
# return the sum of values of all nodes within [low, high]

# we can solve this recursively
# def helper(node, low, high):
# if node < low:
#     node does not qualify (too small), left subtree would not qualify
#     search for right subtree -> helper(node.right, low, high)
# elif node > high:
#     node does not qualify (too large), right subtree would not qualify
#     search for left subtree -> helper(node.left, low, high)
# else:
#     node qualifies, increment val to total
#     helper(node.left, low, high)
#     helper(node.right, low, high) as both left and right subtree could qualify

from Tree import trees
from typing import Optional

class Solution:
    def range_sum_bst(self, root: Optional[trees.TreeNode], low: int, high: int) -> int:
        total = 0

        def helper(node):
            if not node:
                return
            if low <= node.val <= high:
                nonlocal total
                total += node.val
            if node.val > low:
                helper(node.left)
            if node.val < high:
                helper(node.right)

        helper(root)
        return total

    # follow up:
    # multiple queries to get range sum?
