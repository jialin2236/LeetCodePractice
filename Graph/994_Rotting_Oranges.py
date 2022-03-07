"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
import collections
from typing import List


class Solution:
    def rotting_orange(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def neighbors(a, b):
            directions = [(0, 1), (0, -1), (1, 0), (1, -1)]
            for di, dj in directions:
                if 0 <= a + di < n and 0 <= b + dj < n:
                    yield a + di, b + dj

        def bfs():
            nonlocal grid
            status = None

            for row in range(n):
                for col in range(n):
                    val = grid[row][col]
                    n0, n_nei = 0, 0
                    if val == -1:
                        val = 2
                    for ni, nj in neighbors(row, col):
                        nv = grid[ni][nj]
                        if nv == 0:
                            n0 += 1
                        elif nv == 1 and val == 2:
                            nv = -1
                            status = 1
                        elif nv == 2 and val == 1:
                            val = -1
                            status = 1
                        n_nei += 1
                        grid[ni][nj] = nv
                        grid[row][col] = val
                    if val == 1 and n0 == n_nei:
                        return -1
            return 2 if not status else status

        i = 0
        stat = bfs()
        while stat not in [-1, 2]:
            stat = bfs()
            i += 1
        return -1 if stat == -1 else i
