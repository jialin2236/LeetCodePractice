"""
199. Binary Tree Right Side View (M, 112)
"""
from Tree import trees
from typing import Optional, List
from collections import deque

# given root of the tree, return the right side nodes from top to bottom

class Solution:
    def right_side_view1(self, root: Optional[trees.TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        curr_lvl = [root]
        while curr_lvl:
            prev_lvl = curr_lvl
            curr_lvl = []
            for node in prev_lvl:
                if node.left:
                    curr_lvl.append(node.left)
                if node.right:
                    curr_lvl.append(node.right)
            ans.append(node.val)
        return ans

    def right_side_view2(self, root: Optional[trees.TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root, None])
        while queue:
            curr = queue.popleft()
            while curr:
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                prev = curr
                curr = queue.popleft()
            ans.append(prev.val)
            if queue:
                queue.append(None)
        return ans
