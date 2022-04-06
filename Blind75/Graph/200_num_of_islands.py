"""
200. Number of Islands (Medium, 29 fb tagged 0 ~ 6 mth)
https://leetcode.com/problems/number-of-islands/

given an m x n 2D binary array grid, which represents a map of '1's (land) and '0's (water)

return the number of islands. (surrounded by water and is formed by connecting 4-directional neighboring lands)
"""
from typing import List
from collections import deque

# we need to traverse the grid and find the '1's
# do a bfs until no neighboring cell is land
# increment island count


class Solution:
    def num_islands_bfs(self, grid: List[List[str]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        island = 0

        # if we can modify the grid in place
        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                top_i, top_j = queue.popleft()
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nonlocal grid
                    if 0 <= top_i + di < n_row and 0 <= top_j + dj < n_col and grid[top_i + di][top_j + dj] == '1':
                        grid[top_i + di][top_j + dj] = '0'
                        queue.append((top_i + di, top_j + dj))

        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == '1':
                    island += 1
                    grid[row][col] = '0'
                    bfs(row, col)

        return island

    def num_islands_dfs(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        island = 0

        def dfs(i, j):
            nonlocal grid
            grid[i][j] = '0'
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < n_row and 0 <= j + dj < n_col and grid[i][j] == '1':
                    dfs(i + di, j + dj)

        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == '1':
                    island += 1
                    dfs(row, col)

        return island