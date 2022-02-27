"""
261. Graph Valid Tree (Medium)
https://leetcode.com/problems/graph-valid-tree/

You have a graph of n nodes labeled from 0 to n - 1.
You are given an integer n and a list of edges where edges[i] = [ai, bi]
indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
"""
from typing import List

# In general, for a graph to be a valid tree, it needs to meet following criteria
# 1. graph must be fully connected
# 2. no cycle in graph
# From graph theory: there must be (n - 1) edge, < (n - 1) not fully connected, > (n - 1) cycle
# Approach 1
# Using UnionFind
# Approach 2
# DFS while tracking visited nodes

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
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return True
        if self.rank[rootx] > self.rank[rooty]:
            self.root[rooty] = rootx
        elif self.rank[rooty] > self.rank[rootx]:
            self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1
        return False


class Solution:
    def uf_valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False
        uf = UnionFind(n)
        for a, b in edges:
            cycle = uf.union(a, b)
            if cycle:
                return False
        return True

    def dfs_valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: return False

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        parent = {0: -1}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                stack.append(neighbor)
        return len(parent) == n

