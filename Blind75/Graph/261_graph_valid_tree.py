"""
261. Graph Valid Tree (Medium, 0 tagged)
https://leetcode.com/problems/graph-valid-tree/

given n: int as number of nodes in graph, edges: List[List[int]] as undirected edges between pairs of nodes

return bool whether the graph makes up a valid tree
"""
from typing import List
from collections import defaultdict, deque


# properties of a valid tree
# full connected
# no cycle
# 1. number of edges = (number of nodes - 1)
# 2. use bfs/dfs to examine if cycle exists

class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # number of edges == (number of nodes - 1)
        if len(edges) != n - 1:
            return False

        # build a graph using information from edges
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # dfs to find cycle
        # hash set to record nodes visited, as well as avoid parent node to be misidentified as a cycle
        parents = {0: -1}
        queue = deque([0])
        while queue:
            top = queue.pop()
            for node in graph[top]:
                if node == parents[top]:
                    continue
                if node in parents:
                    return False
                parents[node] = top
                queue.append(node)
        return len(parents) == n
