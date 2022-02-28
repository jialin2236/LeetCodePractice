"""
Evaluate Division
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
    def evaluate_division(self, equations: List[List[str]], values: List[int], queries: List[List[str]]) -> List[float]:
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
