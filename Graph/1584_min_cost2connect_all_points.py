"""
1584. Min Cost to Connect All Points (Medium)
tag - MST, Graph, UnionFind, Kruskal's Algorithm

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected.
All points are connected if there is exactly one simple path between any two points.
"""
from collections import defaultdict
import heapq
from typing import List


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
            elif self.rank[ry] > self.rank[rx]:
                self.root[rx] = ry
            else:
                self.root[ry] = rx
                self.rank[ry] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def min_cost2connect_kruskal(self, points: List[List[int]]) -> int:
        n, edges = len(points), []
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(edges, (d, i, j))

        uf = UnionFind(n)
        connects, ans = 0, 0
        while connects < n - 1:
            ec, ei, ej = heapq.heappop(edges)
            if not uf.connected(ei, ej):
                uf.union(ei, ej)
                connects += 1
                ans += ec

        return ans

    def min_cost2connect_prim(self, points: List[List[int]]) -> int:
        n, seen = len(points), set()
        dist_lookup = defaultdict(list)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(dist_lookup[i], (d, j))
                heapq.heappush(dist_lookup[j], (d, i))

        curr = 0
        seen.add(0)
        while len(seen) < n:
            prev = curr
            d, curr = heapq.heappop(dist_lookup[prev])
            while curr in seen:
                d, curr = heapq.heappop(dist_lookup[prev])
            seen.add(curr)
            ans += d

        return ans