"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
Medium

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""
"""
Question:
1. do I move? Meaning that do we need to account for left nodes in the right
subtree?
2. example?
say tree 1:
root.val = 1, root.right.val = 3, root.right.right.val = 4 -> output: [1,3,4]
what if for tree 2:
root.val = 1, root.right.val = 3, root.right.left.val = 2, root.right.right.val = 4 ??
Let's assume we need to account for all nodes from top to bottom in the right subtree 
of root -> move right, perform Breadth First Traversal
if we only need to account for the right subtree of every subtree -> Depth First 
Traversal on all right children
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def right_side_view_assumption2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                if i == level_length - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans

    def right_side_view_assumption1(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            # current level
            curr = queue
            # empty queue to store the next level
            queue = []
            while curr:
                node = curr.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(node.val)
        return ans

    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view

    def rightSideView_i(self, root):
        view = []
        if root:
            level = [root]
            while level:
                view.append(level[-1].val)
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view

