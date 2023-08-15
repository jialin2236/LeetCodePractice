"""
Dijkstra's Algorithm solves the "single-source shortest path" problem in a weighted directed graph
with non-negative weights
"""
from typing import Dict, Tuple
from collections import defaultdict
import heapq


def dijkstra(graph: defaultdict, source: str, target: str) -> Dict[Tuple]:
    seen, remain = defaultdict(Tuple), defaultdict(Tuple)
    seen[source] = (0, None)
    curr, d2s = source, 0
    while target not in seen:
        prev = curr
        for nei, dist in graph[prev].items():
            if nei not in seen or seen[nei][0] < d2s + dist:
                seen[nei] = (d2s + dist, prev)

        curr = min(seen, key=seen.get)
        d2s, adj = remain[curr]
        seen[curr] = (d2s, adj)
        del remain[curr]
    return seen

def dijkstra_heap(graph: defaultdict, source: str, target: str): 
    seen, pq = set(), [(0, source)]
    heapq.heapify(pq)
    while pq: 
        d2s, node = heapq.heappop(pq)
        seen.add(node)
        for dist, nei in graph[node]: 
            if nei not in seen: 
                heapq.heappush((d2s + dist, nei))