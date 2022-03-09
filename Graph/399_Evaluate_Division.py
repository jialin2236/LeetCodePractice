"""
Evaluate Division (Hard)
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3914/

You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.

You are also given some queries,
where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid.
You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

example: equations = [['a', 'b'], ['b', 'c']], values = [2, 3],
         queries = [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]
"""
from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.val = [float(1)] * n

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        self.val[x] = self.val[x] * self.val[self.root[x]]
        return self.root[x]

    def union(self, x, y, v):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.root[ry] = rx
            self.val[ry] = v * (self.val[rx] / self.val[ry])

    def connected(self, x, y):
        rx, ry = self.find(x), self.find(y)
        return self.val[rx]/self.val[ry]


class Solution:
    def evaluate_division_uf(self, equations: List[List[str]], values: List[int], queries: List[List[str]]) -> List[float]:
        """
        solution using UnionFind
        time: O((M+N)logN) - M operations, N elements, union takes O(NlogN), for M queries, find takes O(MlogN)
        space: O(N)
        :param equations:
        :param values:
        :param queries:
        :return:\
        """
        def ch2idx(ch: List[str]):
            base = ord('a')
            res = []
            for c in ch:
                res.append(ord(c) - base)
            return res

        var = set([i for pair in equations for i in ch2idx(pair)])
        n = len(var)
        uf = UnionFind(n)
        for variables, value in zip(equations, values):
            numerator, denominator = ch2idx(variables)
            uf.union(numerator, denominator, value)
        ans = []
        for fi, ti in queries:
            if fi in var and ti in var:
                ans_i = uf.connected(fi, ti)
            else:
                ans_i = float(-1)
            ans.append(ans_i)
        return ans

    def evaluate_division_dfs(self, equations: List[List[str]], values: List[int], queries: List[List[str]]) -> List[float]:
        """
        solution using DFS (graph search) with backtracking technique. For N equations and M queries:
        time: O(M*N) - O(N) to build graph, O(N) to search at each iteration, repeat M times -> O(MN)
        space: O(N) - graph takes O(N) additional space, visited O(N), recurrsion O(N) -> O(3N) -> O(N)
        :param equations:
        :param values:
        :param queries:
        :return:
        """
        graph = defaultdict(defaultdict)
        for (n, d), v in zip(equations, values):
            graph[n][d] = v
            graph[d][n] = 1/v

        def backtracking(curr_node, target_node, curr_value, visited):
            # we can fit our backtracking module to this function
            neighbors = graph[curr_node]
            nonlocal ret
            # if target_node is found, update nonlocal variable ret and exit recursion
            if target_node in neighbors:
                ret = curr_value * neighbors[target_node]
                return
            # otherwise, recursively explore each neighbor path of the curr_node
            for nei, val in neighbors.items():
                # only explore feasible paths (neighbor nodes that has not been visited -> avoid cycle)
                if nei not in visited:
                    visited.add(nei)
                    backtracking(nei, target_node, curr_value * val, visited)
                    visited.remove(nei)

        ans = []
        for n, d in queries:
            if n not in graph or d not in graph:
                ret = -1.0
            elif n == d:
                ret = 1.0
            else:
                seen = {n}
                ret = -1.0
                backtracking(n, d, 1, seen)
            ans.append(ret)
        return ans