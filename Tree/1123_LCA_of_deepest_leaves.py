"""
1123. Lowest Common Ancestor of Deepest Leaves (Medium, 5 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
same as: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/ (Medium, 10 fb tagged 0 ~ 6 months)

Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
"""
from trees import TreeNode
from typing import Optional

# root has depth of 0
# we can traverse down the tree, and record the depth of each node

def lca_deepest_leaves(root: Optional[TreeNode]) -> Optional[TreeNode]:
    lca, max_depth = None, 0

    def find_leaves(node, depth):
        nonlocal max_depth
        max_depth = max(depth, max_depth)
        if not node:
            return depth
        left = find_leaves(node.left, depth + 1)
        right = find_leaves(node.right, depth + 1)
        if left == right == max_depth:
            nonlocal lca
            lca = node
        return max(left, right)

    find_leaves(root, 0)
    return lca