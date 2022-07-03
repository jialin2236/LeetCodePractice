"""
317. Shortest Distance from all buildings (H)
"""
from typing import List
from collections import defaultdict, deque

# input grid: List[List[int]]
# grid[i][j] - 0: empty land, 1: building cannot pass through, 2: obstacle cannot pass through

# find an empty land to build a house on, so that it can reach all houses with the minimum total distance
# return the min total distance from any empty land to all houses, -1 if no such land exists

class Solution:
    def shortest_distance(self, grid: List[List[int]]) -> int:
        # we need to first find out how many buildings there are
        m, n = len(grid), len(grid[0])
        buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    buildings += 1

        def neighbors(x, y):
            for dx, dy in [(1,0), (0,1), (0,-1), (-1,0)]:
                if 0 <= x + dx < m and 0 < y + dy < n:
                    yield x + dx, y + dy

        # create a hash/matrix to store number of buildings each empty land can access to
        #          hash/matrix to store the total distance each empty land to all buildings
        access = defaultdict(int)
        distance = defaultdict(int)

        def bfs(x, y):
            queue = deque([(x, y, 0)])
            visited = {(x, y)}
            reached_buildings = 1
            while queue:
                curr_x, curr_y, dist = queue.popleft()
                for nx, ny in neighbors(curr_x, curr_y):
                    if (nx, ny) not in visited:
                        if grid[nx][ny] == 1:
                            reached_buildings += 1
                        elif grid[nx][ny] == 0:
                            access[(nx, ny)] += 1
                            distance[(nx, ny)] += dist + 1
                            queue.append((nx, ny, dist + 1))
            return reached_buildings == buildings

        # do bfs on each building
        # record each empty land reachable from that building (to)'s distance
        # if a building cannot reach to all other buildings, there is no feasible solution
        # since, no land can reach both buildings
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if not bfs(i, j):
                        return -1

        ans = None
        for i, nb in access.items():
            if nb == buildings:
                ans = distance[i] if not ans else min(ans, distance[nb])
        return ans or -1