"""
547. Number of Provinces (Medium)
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
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
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1


class Solution:
    def num_provinces(self, isConnected: List[List[int]]) -> int:
        """
        dfs solution
        time: O(N^2) - since complete matrix of size n x n is traversed
        space: O(N) worst - since we created a seen set of size n for each city
        :param isConnected:
        :return:
        """
        n = len(isConnected)
        seen = set()

        def dfs(node):
            for neigh, connected in enumerate(isConnected[node]):
                if connected and neigh not in seen:
                    seen.add(neigh)
                    dfs(neigh)

        ans = 0
        for city in range(n):
            if city not in seen:
                dfs(city)
                ans += 1
        return ans

    def num_provinces_uf(self, isConnected: List[List[int]]) -> int:
        """
        union find solution
        time: O(N^3) - Traversal takes O(N^2) time, union and find take O(N) time
        space: O(N) - For root array in uf
        :param isConnected:
        :return:
        """
        n = len(isConnected)
        uf = UnionFind(n)
        for city in range(n):
            for neigh in range(n):
                if city != neigh and isConnected[city][neigh]:
                    uf.union(city, neigh)
        return len(set([uf.find(i) for i in range(n)]))

