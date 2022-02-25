"""
332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/
Hard
"""
"""
construct a graph, start with JFK and do a DFS traversal until 
it reaches a node with no other unvisited neighbor 

1. use defaultdict as graph
2. since problem requires to use each ticket once and exactly once, we can
reduce the problem to finding the Eulerian path

Solution: 
1. backtrack and greedy
2. use greedy DFS
"""
from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]