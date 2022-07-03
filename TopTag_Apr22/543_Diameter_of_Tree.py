"""
543. Diamester of Binary Tree (E, 90)
"""
from Tree import trees
from typing import Optional

# given root of a tree, return the length of the diameter
# max number of edges between any 2 nodes

# can we use recursion?
# for an input node, use recursion function to get the max path of its left and right subtree
# in each recursion run, calculate the max diameter within that subtree, update global result as needed

# ans = -math.inf
#
# def recursion(node):
#     if not node:
#         return
#     left_size = longest path from left subtree leave to left node
#     right_size = longest path from right subtree leave to right node
#
#     node_size = left_size + 1 if left_size else left_size + right_size + 1 if right_size else right_size
#     nonlocal ans
#     ans = max(node_size, ans)
#     return 1 + max(left_size, right_size) if left_size or right_size else 0

# node(4) -> helper(4.left) = 0
#         -> helper(4.right) = 0 -> node size = 1
# node(2) -> helper(2.left) = 1
#         -> helper(2.right) = 1 -> node size = 2
# node(1) -> helper(1.left) = helper(2) = 2
#         -> helper(1.right) = helper(3) = 1 -> node size = 3


class Solution:
    def diameter_of_binary_tree(self, root: Optional[trees.TreeNode]) -> int:
        """
        time: O(n)
        space: O(h)
        :param root:
        :return:
        """
        ans = 0
        if not root:
            return ans

        def helper(node):
            if not node:
                return 0
            left_size = helper(node.left)
            right_size = helper(node.right)

            node_size = left_size + right_size
            nonlocal ans
            ans = max(ans, node_size)
            return 1 + max(left_size, right_size)

        helper(root)
        return ans