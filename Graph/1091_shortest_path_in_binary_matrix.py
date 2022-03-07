"""
1091. Shortest Path in Binary Matrix (Medium)
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected
(i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
"""
import collections
from typing import List, Tuple


class Solution:
    def neighbor(self, idx: Tuple[int, int], n: int):
        x, y = idx
        direction = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0)]
        for i, j in direction:
            if 0 <= x + i < n and 0 <= y + j < n:
                yield x + i, y + j

    def shortest_path(self, grid: List[List]) -> int:
        """
        BFS Approach
        time: O(N) each cell is processed at most once
        space: O(N) to store the queue
        :param grid:
        :return:
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        seen, queue = set(), collections.deque()
        queue.append([(0, 0, 1)])
        seen.add((0, 0))

        while queue:
            head = queue.popleft()
            distance = head.pop()
            for i, j in self.neighbor(head, n):
                if (i, j) not in seen and grid[i][j] == 0:
                    if i == n - 1 and j == n - 1:
                        return distance + 1
                    seen.add((i, j))
                    queue.append((i, j, distance + 1))

        return -1