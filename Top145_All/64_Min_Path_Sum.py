"""
64. Minimum Path Sum
"""
from typing import List

class Solution: 
    def minPathSum(self, grid: List[List[int]]) -> int: 
        m, n = len(grid), len(grid[0])
        dp = [None for _ in range(n)]
        for i in range(m-1, -1, -1): 
            for j in range(n-1, -1, -1): 
                if i == m - 1 and j < n - 1: 
                    dp[j] = dp[j+1] + grid[i][j]
                elif i < m - 1 and j == n - 1: 
                    dp[j] = dp[i+1] + grid[i][j]
                elif i < m - 1 and j < n - 1: 
                    dp[j] = min(dp[j], dp[j+1]) + grid[i][j]
                else: 
                    dp[j] = grid[i][j]