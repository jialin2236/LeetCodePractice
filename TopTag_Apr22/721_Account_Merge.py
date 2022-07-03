"""
721. Account Merge (m)
"""
from typing import List
from collections import defaultdict

# input accounts: List[List[str]]
# given n accounts, accounts[i] = [name_i, email_i1, email_i2, ... ]
# accounts share same email should be merged
# output merged result

# if accounts[i] and accounts[j] have the same email, the 2 accounts need to be merged
# 1. use disjoint set (union find)
class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n

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
                self.rank[rx] += 1

class Solution:
    def account_merge_uf(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        lookup = {}
        for i, info in enumerate(accounts):
            emails = info[1:]
            for e in emails:
                if e in lookup:
                    j = lookup[e]
                    uf.union(i, j)
                lookup[e] = i

        ans = defaultdict(list)
        for email, i in lookup.items():
            j = uf.find(i)
            ans[j].append(email)

        return [[accounts[i][0]] + sorted(val) for i, val in ans.items()]

    def account_merge_dfs(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        n = len(accounts)
        for info in accounts:
            name, emails = info[0], info[1:]
            for i in range(len(emails)):
                for j in range(i + 1, len(emails)):
                    adj[emails[i]].append(emails[j])
                    adj[emails[j]].append(emails[i])

        def dfs(node, ans):
            if node not in visited:
                visited.add(node)
                ans.append(node)
                for nei in adj[node]:
                    if nei not in visited:
                        dfs(nei, ans)
                return ans

        res = []
        visited = set()
        for i in range(n):
            name = accounts[i][0]
            email = accounts[i][1]
            if email not in visited:
                grp = dfs(email, [])
                res.append([name] + sorted(grp))
        return res