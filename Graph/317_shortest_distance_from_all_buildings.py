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

# BFS optimization
# we can modify in place in the grid during each BFS, and mark empty lands that had been reached by the first
# house as -1, and only visit the -1 values (coz otherwise the land could not have been reached by earlier buildings)
# then change from -1 to -2 and perform the next BFS on -1, so on...
# decreased value here can also be used as visited signal.

class Solution:
    def shortest_distance(self, grid: List[List[int]]) -> int:
        """
        time: O(M*N) to traverse the entire grid, at each iteration, BFS takes O(M*N) -> O(M^2 * N^2)
        space: O(M*N) each for hit and distSum, at each iteration, BFS takes O(M*N) for the queue -> O(3M*N)
        :param grid:
        :return:
        """
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

    def shortest_distance_optimized(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        M, N, buildings = len(grid), len(grid[0]), sum([v for row in grid for v in row if v == 1])
        dist_sum = [[0]*N for _ in range(M)]

        def neighbors(x, y):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + dx < M and 0 <= y + dy < N:
                    yield x + dx, y + dy

        def bfs(start_x, start_y):
            queue = collections.deque((start_x, start_y, 0))
            building_count = 1
            while queue:
                hx, hy, hd = queue.popleft()
                for nx, ny in neighbors(hx, hy):
                    if grid[nx][ny] == val:
                        grid[nx][ny] -= 1
                        dist_sum[nx][ny] += (hd + 1)
                        queue.append((nx, ny, hd + 1))
                    elif grid[nx][hy] == 1:
                        building_count += 1
            return building_count == buildings

        val = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if not bfs(i, j): return -1
                val -= 1
        return min([dist_sum[i][j] for i in range(M) for j in range(N) if grid[i][j] == val] or [-1])