"""
1059. All Paths from Source Lead To Destination (Medium)
https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge between nodes ai and bi,
and two nodes source and destination of this graph, determine whether or not all paths starting from source eventually,
end at destination, that is:
1. At least one path exists from the source node to the destination node
2. If a path exists from the source node to a node with no outgoing edges, then that node is equal to destination.
3. The number of possible paths from source to destination is a finite number.

Return true if and only if all roads from source lead to destination
"""
from typing import List
from collections import defaultdict


class Solution:
    def leads2destination(self, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        use dfs by backtracking like logic
        if we go back to a node we had explored in current path, return false
        if we reach the end of the graph, and the end is not destination, return false
        Time: O(V)
        Spcae: O(V+E)
        :param edges:
        :param source:
        :param destination:
        :return:
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)

        seen = set()

        def dfs(node):
            if node not in graph:
                return node == destination
            for nei in graph[node]:
                if nei in seen:
                    return False
                seen.add(nei)
                if not dfs(nei):
                    return False
                seen.remove(nei)
            return True

        return dfs(source)
