"""
1971. Find if path exists in graph

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges,
where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination,
return true if there is a valid path from source to destination, or false otherwise.
"""
import collections
from typing import List
from collections import defaultdict, deque


class Solution:
    def exist_path_dfi(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        seen = set()
        stack = deque()
        stack.append(source)

        while stack:
            top = stack.pop()
            if top == destination:
                return True
            if top not in seen:
                seen.add(top)
                for nei in adj_list[top]:
                    stack.append(nei)
        return False

    def exist_path_dfsr(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node, dest, seen):
            if node not in seen:
                if node == dest:
                    return True
                seen.add(node)
                for nei in adj_list[node]:
                    if dfs(nei, dest, seen):
                        return True
            return False

        return dfs(source, destination, set())

    def exist_path_bfs(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        seen, queue = set(), collections.deque()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        queue.append(source)
        while queue:
            front = queue.popleft()
            if front == destination:
                return True
            if front not in seen:
                for nei in graph[front]:
                    queue.append(nei)
                seen.add(front)
        return False
