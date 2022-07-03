"""
827. Making a Large Island (H, 35)
"""
from typing import List
from collections import deque

# given n x n grid, each cell is 0/1 indicating no-land/land
# change at most one 0 to be 1
# return size of the largest island in grid

# can we do bfs and change cells of an island to the size of the island?
# if grid[i][j] == 1 -> bfs
# def bfs(i, j):
#    for ni, nj in neighbors(i, j):
#        if grid[ni][nj] == 1: add (ni, nj) to set

class Solution:
    def largest_island(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def neighbor(x, y):
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= x + dx < n and 0 <= y + dy < n:
                    yield x+ dx, y + dy

        def bfs(i, j, label):
            res = 1
            queue = deque([(i, j)])
            grid[i][j] = label
            while queue:
                x, y = queue.popleft()
                for nx, ny in neighbor(x, y):
                    if grid[nx][ny] == 1:
                        res += 1
                        grid[nx][ny] = label
                        queue.append((nx, ny))
            return res

        def dfs(i, j, label):
            res = 1
            grid[i][j] = label
            for ni, nj in neighbor(i, j):
                if grid[ni][nj] == 1:
                    res += dfs(ni, nj, label)
            return res

        island, island_size = 2, {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[island] = bfs(i, j, island)
                    # island_size[island] = dfs(i, j, island)
                    island += 1

        ans = max(island_size.values() or 0)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    grp = set()
                    size = 1
                    for ni, nj in neighbor(i, j):
                        if grid[ni][nj] not in grp and grid[ni][nj]:
                            grp.add(grid[ni][nj])
                            size += island_size[grid[ni][nj]]
                    ans = max(ans, size)
        return ans