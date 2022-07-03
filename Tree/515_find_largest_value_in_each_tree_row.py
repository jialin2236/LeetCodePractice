"""
515. Find Largest Value in Each Tree Row (Medium, 24 tagged)
https://leetcode.com/problems/find-largest-value-in-each-tree-row/

given root: Optional[TreeNode], return an array of the largest value in each row of the tree
"""
from typing import Optional, List
from trees import TreeNode
from collections import deque
import math

# Approach
# since we need to compare values in the same row, try BFS
# in BFS, we initiate a queue to put nodes to be traversed into, one by one
#       1
#   3       2
# 5   3         9
# [1] -> [3, 2] -> [2, 5, 3] -> [5, 3, 9] -> ...
# since we need to store levels
# we can add a None element at the end of the level
# queue = deque([root, None])
# while queue:
#   level = []
#   curr = queue.popleft()
#   while curr:
#      until we see a none
#      level.append(curr.val)
#      queue.append(curr.left) queue.append(curr.right)
#      curr = queue.popleft()
#   ans.append(max(level))


class Solution:
    def largest_values(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root, None])
        ans = []
        while queue:
            level_max = -math.inf
            curr = queue.popleft()
            while curr:
                level_max = max(level_max, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                curr = queue.popleft()
            if queue:
                queue.append(None)
            ans.append(level_max)
        return ans
