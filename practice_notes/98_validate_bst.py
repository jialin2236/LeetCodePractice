"""
98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from typing import Optional
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    recursively traverse down the tree
    when hit bottom, return True
    if max of left subtree >= root, return False
    if min of left subtree <= root, return False
    else continue, till hit root, return True
    """

    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                    validate(node.left, low, node.val))

        return validate(root)

    def inorder(self, root: TreeNode, low=-math.inf):
        if not root:
            return
        if not self.inorder(root.left, low):
            return False
        if root.val < low:
            return False
        low = root.val
        return self.inorder(root.right, low)

    def inorder0(self, root: TreeNode):
        low, stack = -math.inf, []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val < low:
                return False
            low = root.val
            root = root.right
        return True
