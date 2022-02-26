"""
827. Making A Large Island 
https://leetcode.com/problems/making-a-large-island/

Medium
"""

"""
you're given an n x n binary matrix grid. you're allowed to change at most one 0 to be 1

return the size of the largest island in grid after applying this operation. 

(an island is a 4-directionally connected group of 1s)
"""

# [[1, 0],       [[1, 0],
#  [0, 1]] -> 3   [1, 1]]
#
# [[1, 1],       [[1, 1],
#  [1, 0]] -> 4   [1, 0]]
#
# [[1, 1],
#  [1, 1]] -> 4 unchanged

# what is directionally connected group? horizontal/vertical? 
# need to determine the size of an island? starting from index i, j
# use dfs to find islands, assign an index to each island
from typing import List
from collections import defaultdict


class Solution:
		def make_large_island(self, grid: List[List[int]]) -> int:
			n = len(grid)
			island_size = defaultdict(int)
			label = 2

			def neighbor(x, y):
				for ni, nj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
					if 0 <= x + ni < n and 0 <= y + nj < n:
						yield x + ni, y + nj

			def valid(x, y):
				if 0 <= x < n and 0 <= y < n:
					return True
				return False

			def dfs(x, y, label):
				if valid(x, y) and grid[x][y] == 1:
					grid[x][y] = label
					island_size[label] += 1
					for ni, nj in neighbor(x, y):
						dfs(ni, nj, label)

			for i in range(n):
				for j in range(n):
					if grid[i][j] == 1:
						dfs(i, j, label)
						label += 1

			ans = 0
			for i in range(n):
				for j in range(n):
					if grid[i][j] == 0:
						neighbor_set = set()
						for nx, ny in neighbor(i, j):
							if valid(nx, ny) and grid[nx][ny] != 0:
								neighbor_set.add(grid[nx][ny])
						island_size0 = 1
						for neighbor_island in neighbor_set:
							island_size0 += island_size[neighbor_island]
						ans = max(ans, island_size0)

			return ans if ans > 0 else n ** 2



# brute force
# def dfs(x, y, seen):
# 	seen.add((x,y))
# 	for xi, yi in neighbor(x, y):
# 		if (xi, yi) not in seen and grid[xi][yi] == 1:
# 			dfs_size(xi, yi, seen)
#
# ans = 0
# for i in range(n):
# 	for j in range(n):
# 		if grid[i][j] == 0:
# 			grid[i][j] = 1
# 			nset = {}
# 			dfs(i, j, nset)
# 			ans = max(ans, len(nset))
# 			grid[i][j] = 0
# return ans if ans > 0 else n ** 2
