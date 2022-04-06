"""
417. Pacific Atlantic Water Flow (Medium, 0 tagged)
https://leetcode.com/problems/pacific-atlantic-water-flow/

m x n rectangular island, borders the pacific on the west and north edge, and the atlantic on the east and south edge.

you're given a 2D array height, height[i][j] indicates the land height at coordinate i, j.

when it rains, rain water can flow from higher land to lower land, into neighboring cells (4-directional).

Return a list of 2D coordinates that can flow water into BOTH the pacific and atlantic.
"""
from typing import List
from collections import deque


# known:
# cells on the north and west edge can flow water to pacific
# cells on the south and east edge can flow water to atlantic
# we can conduct a bfs/dfs on each of those cells, any neighbor that's on a higher land, can have water flown to it

class Solution:
    def pacific_atlantic(self, height: List[List[int]]) -> List[List[int]]:
        n_row, n_col = len(height), len(height[0])
        pacific = set([[0, i] for i in range(n_col)]).union(set([[j, 0] for j in range(n_row)]))
        atlantic = set([[n_row - 1, i] for i in range(n_col)]).union(set([[j, n_col - 1] for j in range(n_row)]))

        def bfs(x, y, seen, ocean):
            queue = deque([(x, y)])
            while queue:
                i, j = queue.popleft()
                seen.add((i, j))
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= i + di < n_row and 0 <= j + dj < n_col and (i + di, j + di) not in seen:
                        if height[i + di][j + dj] > height[i][j]:
                            ocean.add([i + di, j + dj])
                            queue.append((i + di, j + dj))

        seen = set()
        for pi, pj in pacific:
            bfs(pi, pj, seen, pacific)

        seen.clear()
        for ai, aj in atlantic: 
            bfs(ai, aj, seen, atlantic)

        return [coordinates for coordinates in pacific if coordinates in atlantic]
