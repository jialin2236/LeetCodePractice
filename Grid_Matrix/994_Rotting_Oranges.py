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
    def __init__(self, grid: List[List[int]]):
        self.row = len(grid)
        self.col = len(grid[0])

    def neighbors(self, a, b):
        directions = [(0, 1), (0, -1), (1, 0), (1, -1)]
        for di, dj in directions:
            if 0 <= a + di < self.row and 0 <= b + dj < self.col:
                yield a + di, b + dj

    def rotting_orange_inplace(self, grid: List[List[int]]) -> int:
        """
        Time: O(N^2)
        Space: O(1)
        :param grid:
        :return:
        """
        n = len(grid)

        def bfs():
            nonlocal grid
            status = None

            for r in range(n):
                for c in range(n):
                    val = grid[r][c]
                    n0, n_nei = 0, 0
                    if val == -1:
                        val = 2
                    for ni, nj in self.neighbors(r, c):
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
                        grid[r][c] = val
                    if val == 1 and n0 == n_nei:
                        return -1
            return 2 if not status else status

        i = 0
        stat = bfs()
        while stat not in [-1, 2]:
            stat = bfs()
            i += 1
        return -1 if stat == -1 else i

    def rotting_oranges(self, grid: List[List[int]]) -> int:
        """
        time: O(N)
        space: O(N)
        :param grid:
        :return:
        """
        queue = collections.deque()

        fresh_oranges = 0
        for r in range(self.row):
            for c in range(self.col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        queue.append((-1, -1))

        timestamp = -1
        while queue:
            r, c = queue.popleft()
            if r == -1:
                timestamp += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for nei_r, nei_c in self.neighbors(r, c):
                    if grid[nei_r][nei_c] == 1:
                        grid[nei_r][nei_c] = 2
                        fresh_oranges -= 1
                        queue.append((nei_r, nei_c))

        return timestamp if fresh_oranges == 0 else -1