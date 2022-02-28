"""
1101. The Earliest Moment When Everyone Become Friends (Medium)
https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

There are n people in a social group labeled from 0 to n - 1.
You are given an array logs where logs[i] = [timestampi, xi, yi]
indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a.
Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person.
If there is no such earliest time, return -1
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
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return True
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        return False


class Solution:
    def earliest_acq(self, logs: List[List[int]], n: int) -> int:
        # need at least n - 1 events to connect everything
        if len(logs) < (n - 1): return -1
        # initiate n_group to be the same as number of people, as UnionFind merges
        # disjoint sets together, decrement n_group (not decrement when 2 nodes are already connected)
        uf = UnionFind(n)
        logs.sort(key=lambda x: x[0])
        n_group = n
        for ts, a, b in logs:
            connected = uf.union(a, b)
            if not connected:
                n_group -= 1
                if n_group == 1:
                    return ts
        return -1
