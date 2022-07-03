"""
536. Construct Binary Tree from String (M)
"""
from Tree import trees
from typing import Optional

# input s: str
# s consists of parenthesis and integers
# it represents a binary tree. int(int(int)int(int)) or int or int(int)
# int: root's value, (int) child binary tree
# left child node of the parent first if it exists

# if a node has descendent, it'll always have left child, but not always have right child
# could the input be empty?

# input s: str
# if s is empty: return empty
# otherwise:
# first integer is the value of tree root
# i = 0
# while i < len(s):
#     if s[i] != '(': i += 1
# first_integer = s[:i]
# root = Node(first_integer)

   #      4
   #    /   \
   #   2     6
   #  / \   /
   # 3   1  5

# 4(2(3)(1))(6(5))
# since structure is the same, we can use recursion here
class Solution:
    def str2tree(self, s: str) -> Optional[trees.TreeNode]:
        def helper(i: int, j: int) -> Optional[trees.TreeNode]:
            """
            :param i: start index of the tree(subtree) we're building
            :param j: ending index of the tree(subtree) we're building
            :return: root node of the tree(subtree) built
            """
            # 1. find the value of subtree root value -> find i where s[i] is the first '(' in s[i:j]
            i0 = i
            while s[i] != '(' and i < j:
                i += 1
            # if there's no '(' -> the node is a leaf node
            if i == j: return trees.TreeNode(int(s[i0:j]))
            node = trees.TreeNode(int(s[i0:i]))
            # 2. find substring of s[i:j] that represent the left child and right child
            # by matching parenthesis
            i += 1
            i0, opens = i, 1
            while opens > 0:
                if s[i] == '(': opens += 1
                elif s[i] == ')': opens -= 1
            # if i is at the end of the substring -> i == j -> there is no right child
            node.left = helper(i0, i-1)
            if i < j: node.right = helper(i+2, j-1)
            return node
        
        return helper(0, len(s))