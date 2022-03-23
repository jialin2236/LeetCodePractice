"""
317. shortest distance from all buildings (Hard)
https://leetcode.com/problems/shortest-distance-from-all-buildings/

given an m x n grid, grid[i][j] in [0,1,2]
0 - empty land, can pass by freely
1 - building, cannot pass
2 - obstacle, cannot pass

find an empty land to build a house on. so that, it reaches all buildings in the shortest total travel distance.
(can move 4-directionally). return minimal distance, if not feasible, return -1

total distance: sum of manhattan distance to each building
"""
import collections
from typing import List

# use BFS, start from each building, and calculate its distance to each empty land
# if a building cannot reach to all buildings, it's not feasible, return -1

class Solution:
    def shortest_distance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit, distSum = [[0] * N for _ in range(M)], [[0] * N for _ in range(M)]

        def neighbors(x, y):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < M and 0 <= y + dy < N:
                    yield x + dx, y + dy

        def BFS(start_x, start_y):
            visited, queue = [[False] * N for _ in range(M)], collections.deque([(start_x, start_y, 0)])
            visited[start_x][start_y] = True
            building_count = 1
            while queue:
                x, y, dist = queue.popleft()
                for xi, yi in neighbors(x, y):
                    if not visited[xi][yi]:
                        visited[xi][yi] = True
                        if not grid[xi][yi]:
                            queue.append((xi, yi, dist + 1))
                            hit[xi][yi] += 1
                            distSum[xi][yi] += dist + 1
                        elif grid[xi][yi] == 1:
                            building_count += 1
            return building_count == buildings

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if not BFS(i, j): return -1

        return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])