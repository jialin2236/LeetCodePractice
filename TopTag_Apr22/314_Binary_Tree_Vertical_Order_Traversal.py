"""
314. Binary Tree Vertical Order Traversal (M, 193)
"""
from Tree import trees
from typing import Optional, List
from collections import defaultdict
from math import inf

# what we know?
# input - root (TreeNode)
# need vertical order traversal output
# Vertical Order Traversal: top -> bottom, col by col (?)
# nodes in same row and col, left to right

# example
#     3
#  9     20
#     15    7
# -> [[9], [3, 15], [20], [7]]

# use dfs traversal but keep row and col index at the same time
# root, (0, 0)
# root.left, (1, -1)
# number of nodes is 1- 100, we can keep a hash_map to store nodes' row and col index, it would not
# create too much additional space memory

# since nodes in same row and col should be returned left -> right, let's do inorder traversal for this


def vertical_order(root: Optional[trees.TreeNode]) -> List[List[int]]:
    """
    time: O(W*H*logH) - N for dfs traversal, then iterate over n_col to build the answer + sort
                       = N + num_col*H*logH -> N + W*H*logH -> W*H*logH
    space: O(N) - N for the recursion, N for the hash map = 2N -> N
    :param root:
    :return:
    """
    nodes_lookup = defaultdict(list)
    min_col, max_col = int(inf), int(-inf)

    def dfs(node: Optional[trees.TreeNode], row, col):
        if node:
            nonlocal min_col, max_col
            min_col = min(col, min_col)
            max_col = max(col, max_col)
            nodes_lookup[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

    ans = []
    dfs(root, 0, 0)
    for c in range(min_col, max_col + 1):
        # sort each col by their rows
        # in-place
        nodes_lookup[c].sort(key=lambda x: x[0])
        ans.append([v for r, v in nodes_lookup[c]])
    return ans