"""
129. Sum Root to Leaf Numbers (Medium, 31 tagged)
https://leetcode.com/problems/sum-root-to-leaf-numbers/

given root of a tree
return the total sum of all root-to-leaf numbers.
root-to-leaf path 1->2->3 represents number 123
"""
import Tree.trees
from Tree import trees
from typing import Optional
from collections import deque


# we can use dfs to traverse the tree
# root -> left -> right

class Solution:
    def sum_numbers_recursive(self, root: Optional[trees.TreeNode]) -> int:
        """
        time: O(N)
        space: O(H)
        :param root:
        :return:
        """
        total = 0
        if not root:
            return total

        def dfs(node, value):
            value = 10*value + node.val
            if not (node.left or node.right):
                # node is a leaf node
                nonlocal total
                total += value
                return
            if node.left:
                # node is not a leaf node and has left child
                dfs(node.left, value)
            if node.right:
                # node is not a leaf node and has right child
                dfs(node.right, value)

        dfs(root, 0)
        return total

    def sum_numbers_iterative(self, root: Optional[trees.TreeNode]) -> int:
        total = 0
        # stack to store (node, cumulative_val)
        stack = deque([(root, 0)])

        while stack:
            node, curr = stack.pop()
            curr = curr * 10 + node.val
            if not (node.left or node.right):
                total += curr
            if node.left:
                stack.append((node.left, curr))
            if node.right:
                stack.append((node.right, curr))

        return total