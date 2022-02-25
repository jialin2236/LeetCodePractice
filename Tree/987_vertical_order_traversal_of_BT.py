"""
987. Vertical Order Traversal of a Binary Tree 
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

Hard
"""

"""
given the root of a binary tree, calculate the vertical order traversal of the binary tree 

for each node at position (row, col), its left and right children will be at positions 
(row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0)

the vertical order traversal of a binary tree is a list of top-to-bottom orderings for each 
column index starting from the leftmost column and ending on the rigthmost column. There may
be multiple nodes in the same row and column. In such a case, sort these nodes by their values.

return the vertical order traversal of the binary tree. 
"""

# use DFS to traverse the tree. keep track of the min and max col the traversal have seen so far
# use a hash map to store values at each column
def verticalTraversal(root): 
	col_map = collections.defaultdict(list)
	minc, maxc = 0, 0 

	def dfs(node, col, row): 
		if node: 
			col_map[col].append((row, value))
			minc = min(minc, col)
			maxc = max(maxc, col)
			dfs(node.left, col - 1, row + 1)
			dfs(node.right, col + 1, row + 1)

	dfs(root, 0, 0)
	ans = []
	for c in range(minc, maxc + 1): 
		# as required sort all elements in a column by row number, value
		ans.append([v for r, v in sorted(col_map[c])])
	return ans 
