"""
743. Network Delay Time (Medium)
https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node,
and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal.
If it is impossible for all the n nodes to receive the signal, return -1.
"""
import heapq
import math
from typing import List
from collections import defaultdict


class Solution:
    def network_delay_time(self, n: int, k: int, times: List[List[int]]) -> int:
        """
        Dijkstra Algorithm to find shortest path in a positive weighted directed graph
        time: O(E + NlogN)
        space: O(N)
        :param n:
        :param k:
        :param times:
        :return:
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u-1].append((v - 1, w))

        seen, remain = set(), [math.inf for i in range(n)]
        priority_q = []
        heapq.heapify(priority_q)
        remain[k - 1] = 0
        heapq.heappush(priority_q, (0, k - 1))
        ans = 0

        while priority_q:
            curr, curr_d2s = heapq.heappop(priority_q)
            ans += curr_d2s
            seen.add(curr)
            for nei, nei_d2curr in graph[curr]:
                if nei not in seen:
                    nei_d2s = curr_d2s + nei_d2curr
                    if remain[nei] > nei_d2s:
                        remain[nei] = nei_d2s
                        heapq.heappush(priority_q, (nei_d2s, nei))

        return -1 if len(seen) < n else ans