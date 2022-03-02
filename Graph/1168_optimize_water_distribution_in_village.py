"""
1168. Optimize Water Distribution in a Village (Hard)
https://leetcode.com/problems/optimize-water-distribution-in-a-village/

There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing),
or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each
pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe.
Connections are bidirectional, and there could be multiple valid connections between the same two houses with different
costs.

Return the minimum total cost to supply water to all houses.
"""
import heapq
from typing import List
from collections import defaultdict


class Solution:
    def min_cost2supply_water_prims(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
        minimum spanning tree (mst) using Prim's algorithm
        time: O((M+N)log(M+N)) - adjacency list cost O(M+N), worst case we iterate all edges (M+N), and push into
              priority queue O(log(M+N)) -> O((M+N)log(M+N))
        space: O(M+N) - adjacency list O(N+M), set O(N), mst heap O(M+N)
        :param n:
        :param wells:
        :param pipes:
        :return:
        """
        # adjacency list to represent the bidirectional graph
        graph = defaultdict(list)

        # virtual node 0 to represent a virtual starting vertex, connected
        # to each house by the cost to build a well there
        for house, cost in wells:
            graph[0].append((cost, house + 1))

        for house1, house2, cost in pipes:
            graph[house1].append((cost, house2))
            graph[house2].append((cost, house1))

        # a set to maintain all vertices that's been added
        mst = {0}
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        total_cost = 0
        while len(mst) < n + 1:
            cost, next_house = heapq.heappop(edges_heap)
            if next_house not in mst:
                mst.add(next_house)
                total_cost += cost
                # expand candidates of edge to choose from in the next round
                for new_cost, nei_house in graph[next_house]:
                    if nei_house not in mst:
                        heapq.heappush(edges_heap, (new_cost, nei_house))

        return total_cost

    def min_cost2supply_water_kruskal(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
        minimum spanning tree (mst) using kruskal algorithm
        time: O((M+N)log(M+N)) - build ordered_edge takes O(M+N), sort ordered_edge takes O((M+N)log(M+N)),
              UnionFind takes O((M+N)logN) -> O((M+N)log(M+N))
        space: O(M+N) - ordered_edges takes O(M+N), union sort takes O(2N)
        :param n:
        :param wells:
        :param pipes:
        :return:
        """
        ordered_edges = []
        # add virtual vertex (0) with the new edges (cost to build well at each house)
        for house, cost in enumerate(wells):
            ordered_edges.append((cost, 0, house + 1))

        # add pipe edges
        for house1, house2, cost in pipes:
            ordered_edges.append((cost, house1, house2))

        ordered_edges.sort(key=lambda x: x[0])

        uf = UnionFind(n)
        total_cost = 0
        for cost, house1, house2 in ordered_edges:
            # do not add edge when it creates a cycle
            if uf.union(house1, house2):
                total_cost += cost

        return total_cost


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        return True
