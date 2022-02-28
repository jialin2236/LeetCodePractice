"""
323. Number of Connected Components in an Undirected Graph (Medium)
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge between ai and bi in the graph.

Return the number eof connected components in the graph
"""
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
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
            elif self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            else:
                self.root[ry] = rx
                self.rank[rx] += 1


class Solution:
    def n_components_uf(self, n: int, edges: List[List[int]]) -> int:
        """
        time: O(E) - iterate over edges
        space: O(V) - to store the root and rank of the UnionFind
        :param n:
        :param edges:
        :return:
        """
        # use UnionFind to connect nodes in edges, answer would be the number of unique roots
        uf = UnionFind(n)
        for a, b in edges:
            uf.union(a, b)
        root_set = set([uf.find(i) for i in range(n)])
        return len(root_set)

    def n_components_dfs(self, n: int, edges: List[List[int]]) -> int:
        """
        time: O(E + V) - O(E) to build adjacency list, dfs visits each vertex once.
        space: O(E + V) - O(E) for adjacency list, dfs uses seen set takes O(V)
        :param n:
        :param edges:
        :return:
        """
        # use dfs, build adjacency list and use dfs to build connected components
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        seen = set()

        def dfs(node):
            for nei in adj_list[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans


