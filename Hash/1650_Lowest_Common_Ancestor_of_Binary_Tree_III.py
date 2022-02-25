"""
1650. Lowest Common Ancestor of a Binary Tree III
Medium

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the
lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def LowestCommonAncestor(self, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time: O(N)
        Space: O(N)
        :param p:
        :param q:
        :return:
        """
        parents = set()
        while p:
            parents.add(p)
            p = p.parent
        while q not in parents:
            q = q.parent
        return q

    def LowestCommonAncestor0(self, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Time: O(N)
        Space: O(1)
        :param p:
        :param q:
        :return:
        """
        p1, q1 = p, q
        while p1 != q1:
            p1 = p1.parent if p1 else q
            q1 = q1.parent if q1 else p
        return p1