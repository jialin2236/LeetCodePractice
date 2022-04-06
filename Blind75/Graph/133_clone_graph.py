"""
133. Clone Graph (Medium, 44 fb tagged 0~6 mth)
https://leetcode.com/problems/clone-graph/

given a reference of a node in a connected undirected graph.

return a deep copy of the graph
"""
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def clone_graph_bfs(self, node: Optional[Node]) -> Optional[Node]:
        """
        BFS solution to traverse and copy graph
        time: O(V+E)
        space: O(V+E)
        :param node:
        :return:
        """
        if not node:
            return node
        visited = {}
        node_copy = Node(node.val)
        visited[node] = node_copy
        queue = deque([node])
        while queue:
            head = queue.popleft()
            for nei in head.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    queue.append(nei)
                visited[head].neighbors.append(visited[nei])
        return visited[node]

    def clone_graph_dfs(self, node: Optional[Node]) -> Optional:
        visited = {}
        def dfs(node):
            if not node:
                return node
            if node in visited:
                return visited[node]
            copy_node = Node(node.val)
            visited[node] = copy_node
            for nei in node.neighbors:
                dfs(nei)
            return copy_node
        return dfs(node)