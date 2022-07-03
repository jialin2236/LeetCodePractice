"""
1091. Shortest Path in Binary Matrix (m, 67)
"""
from typing import List
from collections import deque

# given grid: List[List[int]] of n x n
# find shortest path (8-directional per step) from (0,0) to (n-1,n-1)

# shortest path from source to destination
# unweighted, undirected graph -> bfs

class Solution:
    def neighbor(self, x, y, n):
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            if 0 <= x + dx < n and 0 <= y + dy < n:
                yield x + dy, y + dy

    def shortest_path_binary_mat(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1

        # bfs without changing grid values
        queue = deque([(0, 0, 1)])
        seen = {(0, 0)}
        while queue:
            x, y, d2s = queue.popleft()
            if (x, y) == (n - 1, n - 1):
                return d2s
            for nx, ny in self.neighbor(x, y, n):
                if (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny, d2s + 1))
        return -1

    def shortest_path_binary_mat_faster(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1

        # bfs with modifying grid value
        queue = deque([(0,0)])
        grid[0][0] = 1
        while queue:
            i, j = queue.popleft()
            d2s = grid[i][j]
            if (i, j) == (n-1, n-1):
                return d2s
            for ni, nj in self.neighbor(i, j, n):
                if not grid[ni][nj]:
                    queue.append((ni, nj))
                    grid[ni][nj] = d2s + 1
        return -1