from typing import List
from collections import defaultdict

# Using UnionFind to build disjoint set
# Time Complexity: O(N^2) as a result of constructing disjoint set by traversing the grid
# Space Complexity: O(N^2) to store the disjoint set (in fact 2N^2)

class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        root_x = self.root[x]
        root_y = self.root[y]
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.root[root_x] += 1
            return True
        else:
            return False

class Solution:
    def make_a_island(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        uf = UnionFind(n * n)

        def neighbor(x, y):
            for r, c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x + r < n and 0 <= y + c < n:
                    yield x + r, y + c

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for ni, nj in neighbor(i, j):
                        if grid[ni][nj]:
                            uf.union(n * i + j, n * ni + nj)

        area = defaultdict(int)
        for i in range(n * n):
            root_i = uf.find(i)
            area[root_i] += 1

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    root_ij = uf.find(n * i + j)
                    ans = max(ans, area[root_ij])
                else:
                    incr = 1
                    seen = set()
                    for ni, nj in neighbor(i, j):
                        if grid[ni][nj]:
                            root_ij = uf.find(n * ni + j)
                            if root_ij not in seen:
                                seen.add(root_ij)
                                incr += area[root_ij]
                    ans = max(ans, incr)
        return ans


