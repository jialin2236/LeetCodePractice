"""
133. Clone Graph (Medium)
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
"""
from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = 0
        self.neighbors = neighbors if neighbors else []


class Solution:
    def __init__(self):
        self.seen = {}

    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return
        if node in self.seen:
            return self.seen[node]
        clone_node = Node(node.val)
        self.seen[node] = clone_node
        if node.neighbors:
            clone_node.neighbors = [self.clone_graph(nei) for nei in node.neighbors]
        return clone_node
