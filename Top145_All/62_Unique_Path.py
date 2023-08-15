"""
62. Unique Paths
"""

# input m: int, n: int
# m, n represent number of rows and col in a matrix
# return number of unique paths one could take to go from (0,0) to (m-1,n-1)
# you can only go right or down 


# total steps one would need to take = (m-1) + (n-1)
# out of which, m - 1 of them would be down, n - 1 be right
# -> choose (m-1)/(n-1) out of (m + n - 2), number of combinations

class Solution: 
    def unique_paths_dp(self, m: int, n: int) -> int: 
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m): 
            for j in range(1, n): 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

    def unique_paths_math(self, m: int, n: int) -> int: 
        hi = (m + n - 2)
        lo = min(m-1, n-1)
        res = 1
        while lo: 
            res *= hi
            res /= lo
            hi -= 1
            lo -= 1
        return res