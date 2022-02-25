"""
314. Binary Tree Vertical Order Traversal 
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Medium 
"""

# given the root of a binary tree, return the vertical order traversal of its 
# nodes' values (top to bottom, column by column)
# if 2 nodes are in the same row and column, order should be left to right

# could the tree be empty?
# is the tree balanced? 
# 	  3
#   9        20
#    2  15  7
#   1 4

# modified in order traversal
# recurse to the left most child of root; 
# add nodes to a stack along the way, with its relative distance to root  
# [(3,0), (9, -1)] when reached the left most child,
# pop 9, if 9 has any right child. recursive the right child's left subtree. 
# def left_subtree(node, distance_to_root)
# when reached right subtree's left most child, pop it one by one, 
# compare it with (9, -1)

# find the left subtree
# stack = [(3,0), (9,-1), (4,-2)]
# # when found left most
# stack.pop -> top = (4, -2)
# ans += top # ans = [(4,-2)]
# if top[0].right (has right child)
# # find its left substree
# # else stack.pop -> top = (9, -1)
# if top[0].right (has right child)
# # add left subtree to stack = [(3,0)]
# stack = [(3, 0), (0, 0), (5, -1)] # found left most
# # if top = stack.pop has right child -> left subtree that, else
# ans += top (5, -1) # ans = [(4,-2), (5,-1)], stack = [(3,0),(0,0)]
# # stack.pop() as top, repeat if top has right child, left_subtree
from collections import defaultdict
from typing import Optional

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution:
	def vertical_traverse(self, root: Optional[Node]):
		min_col, max_col = 0, 0

		def traverse(node, row, col, table):
			if node:
				nonlocal min_col, max_col
				table[col].append((row, node.val))
				min_col = min(min_col, col)
				max_col = max(max_col, col)
				traverse(node.left, row + 1, col - 1, table)
				traverse(node.right, row + 1, col + 1, table)

		if not root:
			return []
		lookup = defaultdict(list)
		min_col, max_col = 0, 0
		traverse(root, 0, 0, lookup)
		ans = []
		for column in range(min_col, max_col + 1):
			lookup[column].sort(key=lambda x: x[0])
			ans.append([v for r, v in lookup[column]])
		return ans


