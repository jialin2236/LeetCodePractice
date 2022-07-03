"""
236. Lowest Common Ancestor of Binary Tree (M, 179)
"""
from collections import deque
from Tree import trees

# build a parent hash to record all parents of all nodes
# rest is the same as 1650

class Solution:
    def build_parents(self, root):
        parents = {root: None}
        queue = deque([root])
        while queue:
            top = queue.popleft()
            if top.left:
                parents[top.left] = top
                queue.append(top.left)
            if top.right:
                parents[top.right] = top
                queue.append(top.right)
        return parents

    def lowest_common_ancestor(self, root: trees.TreeNode, p: trees.TreeNode, q: trees.TreeNode) -> trees.TreeNode:
        parents = self.build_parents(root)
        ancestors = set()
        curr = p
        while curr:
            ancestors.add(curr)
            curr = parents[curr]
        curr = q
        while curr not in ancestors:
            curr = parents[curr]
        return curr

    def lca_o1_memory(self, root: trees.TreeNode, p: trees.TreeNode, q: trees.TreeNode) -> trees.TreeNode:
        parents = self.build_parents(root)
        p0, q0 = p, q
        while p != q:
            p = parents[p] if parents[p] else q0
            q = parents[q] if parents[q] else p0
        return p