"""
1650. Lowest Common Ancestor of a Binary Tree III (M, 138)
"""

# what we know
# TreeNode class has val, left, right, parent available
# given 2 nodes
# return the LCA node

# Approach
# since we know each node's parent, we can build the ancestor path of one of the nodes
# and search up the other node's parent path, as soon as they have a common node in the path
# that's their LCA

from Tree import trees
from typing import Optional

class Solution:
    def LCA(self, p: Optional[trees.TreeNode], q: Optional[trees.TreeNode]) -> Optional[trees.TreeNode]:
        """
        time: worse O(H) - O(2H)
        space: worse O(H)
        :param p:
        :param q:
        :return:
        """
        if not (p and q):
            return None
        curr = p
        ancestor = set()
        while curr:
            ancestor.add(curr)
            curr = curr.parent
        curr = q
        while curr not in ancestor:
            curr = curr.parent
        return curr

    def LCA1(self, p: Optional[trees.TreeNode], q: Optional[trees.TreeNode]) -> Optional[trees.TreeNode]:
        """
        time: worst O(H)
        space: O(1)
        0 -> 2 -> 3 -> 4 -> 5 -> 10
                            |
             6 -> 7 -> 8 -->
        :param p:
        :param q:
        :return:
        """
        if not (p and q):
            return None
        p0, q0 = p, q
        while p != q:
            p = p.parent if p.parent else q0
            q = q.parent if q.parent else p0
        return p