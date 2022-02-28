"""
Smallest String with Swaps
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3913

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b]
indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
"""
from typing import List
from collections import defaultdict


class UnionFind:
    """
    could be optimized by using Union By Rank
    """
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.root[rx] = ry


class Solution:
    def smallest_str_w_swaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Time: O(N) to construct UF, O(logN) to union, O(logN) to find. O(N) to build s_connect, O(NlogE) to sort, O(N)
        Space: O(N) for UF, O(N) for rts, O(N) for s_connected, O(N) for s_sorted
        :param s:
        :param pairs:
        :return:
        """
        n = len(s)
        uf = UnionFind(n)
        for a, b in pairs:
            uf.union(a, b)
        s_connected = defaultdict(list)
        rts = [uf.find(i) for i in range(n)]
        for idx, g in enumerate(rts):
            s_connected[g].append(idx)
        s_sorted = {}
        for grp in s_connected:
            s_sorted[grp] = sorted([s[i] for i in s_connected[grp]])
        ans = []
        for i in range(n):
            grp_i = rts[i]
            val = s_sorted[grp_i].pop(0)
            ans.append(val)
        return ''.join(ans)
