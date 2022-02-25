"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Easy
"""

# given the root node of a bst and 2 integers low and high
# return the sum of values of all nodes with a value in the inclusive 
# range [low, high]

# take advantage of the BST structure
# root.left < root < root.right
# given the low and high
# start from the root, 
# if root < low -> we only need to traverse the right subtree
# if root > high -> we only need to traverse the left subtree
# else (low < root < high) -> left subtree with lower bound, 
# right subtree with upper bound

def rangeSumBST_r(root, low, high):
	ans = 0
	def include(node, lb, ub):
		if node: 
			if lb <= node.val <= ub:
				nonlocal ans
				ans += 1
			if node.val > lb:
				include(node.left, lb, ub)
			if node.val < ub: 
				include(node.right, lb, ub) 

	include(root, low, high)
	return ans


# iterative
def rangeSumBST_i(root, low, high): 
	ans = 0
	stack = [root] if low <= root.val <= high else []
	while stack:
		node = stack.pop()
		if node: 
			ans += node.val 
			if node.left and node.left.val >= low: 
				stack.append(node.left)
			if node.right and node.right.val <= high: 
				stack.append(node.right)
	return ans 
