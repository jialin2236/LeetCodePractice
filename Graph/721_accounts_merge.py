"""
721. Accounts Merge (Medium)
https://leetcode.com/problems/accounts-merge/

given:
list of accounts, accounts[i]: [name, email1, email2, ...]
task:
merge accounts, if two accounts have the same email, they belong to the same person (all of those accounts will
have the same name)
output:
list of merged accounts, emails in sorted order for each person
"""
import collections
from typing import List
# ["john", "johnsmith@mail.com", "john@mail.com"], ["john", "john@mail.com"] is the same person
# ["john", "john00@mail.com"], ["john", "johnnybravo@mail.com"] are not the same person


# use a disjoint set
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
            elif self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            else:
                self.root[ry] = rx
                self.rank[rx] += 1


class Solution:
    def account_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        emails_map = {}
        uf = UnionFind(n)
        for idx in range(n):
            name, emails = accounts[idx][0], accounts[idx][1:]
            for email in emails:
                if email in emails_map:
                    uf.union(idx, emails_map[email])
                emails_map[email] = idx

        ans = collections.defaultdict(list)
        for email, i in emails_map.items():
            ans[uf.find(i)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

