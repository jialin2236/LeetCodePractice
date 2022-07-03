"""
269. Alien Dictionary (M, 18)
"""
from typing import List
from collections import defaultdict, deque

class Solution:

# since elements in words are sorted lexicographically
# we can use thier relationship to derive certain lexicographical orders
# ex: [w1, w2] at index i, if w1[:i] == w2[:i] and w1[i] != w2[i] -> w1[i] is smaller than w2[i]
# build a graph using this relationship, with char as nodes, and lexicographical order as directed edges

    def alien_order(self, words: List[str]) -> str:
        """
        time: n - number of words   c - total character length of words     u - size of unique characters
              1. traversing the words and building graph and in_degree O(c)
              2. using bfs to topologically sort the graph O(v + e) = O(u + n) / O(u + u^2)
        :param words:
        :return:
        """
        graph = defaultdict(set)
        in_degree = {c: 0 for w in words for c in w}

        for w1, w2 in zip(words[:-1], words[1:]):
            size = min(len(w1), len(w2))
            for i in range(size):
                if w1[:i] == w2[:i] and w1[i] != w2[i]:
                    graph[w1[i]].add(w2[i])
                    in_degree[w2[i]] += 1
                    break

        queue = deque([c for c, i in in_degree.items() if i == 0])
        ans = []
        while queue:
            ch = queue.popleft()
            ans.append(ch)
            for n in graph[ch]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)

        return ''.join(ans) if len(ans) == len(in_degree) else ''
