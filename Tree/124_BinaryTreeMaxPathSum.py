"""
124. Binary Tree Maximum Path Sum
"""
from math import inf 
from typing import Optional
from trees import TreeNode

# path: sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them
# a node can only appear once in a path
# path sum: sum of the nodes values in the path
# return max path sum

class Solution: 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -inf

        def helper(node):
            nonlocal max_sum
            if not node: 
                return 0
            l = max(helper(node.left), 0)
            r = max(helper(node.right), 0)
            max_sum = max(max_sum, l + r + node.val)
            return max(l, r) + node.val
        
        helper(root)
        return max_sum
         
