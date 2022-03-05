"""
797. All Paths from Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).
"""
import collections
from typing import List


class Solution:
    """
    for both solutions (DFS, BFS):
    time: O(2^V * V) - there could be 2^(V-1) - 1 possible paths to go from source to destination, we need O(V)
          time to build each path
    space: O(2^V * V) - for the queue/recursion  
    """
    def paths_from_s2t(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []

        def dfs(curr, path):
            if curr == n - 1:
                # copy the path before appending it to the solution is crucial in recursive backtracking
                ans.append(path.copy())
                return
            for nxt in graph[curr]:
                path.append(nxt)
                dfs(nxt, path)
                path.pop()

        dfs(0, [0])
        return ans

    def paths_from_s2t_bfs(self, graph: List[List[int]]) -> List[List[int]]:
        n, ans = len(graph), []
        queue = collections.deque()
        queue.append([0])

        while queue:
            top = queue.popleft()
            top_end = top[-1]
            if top_end == n - 1:
                ans.append(top)
                continue
            for nei in graph[top_end]:
                n = top + [nei]
                queue.append(n)

        return ans
