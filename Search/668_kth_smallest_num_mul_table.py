"""
668. Kth Smallest Number in Multiplication Table (Hard)
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/

The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
"""

# option 1
# we can use a min heap while we traverse through the multiplication table
# but this would have m*n space complexity, m*nlog(m*n) time complexity
# option 2
# we know that the lower bound of the elements is 1, while the upper bound is m * n
# instead of iterating through the entire table, we can use binary search to look for the
# Kth smallest number in the table


class Solution:
    def find_kth_num(self, m: int, n: int, k: int) -> int:
        def enough(x: int) -> bool:
            # determine if there are more than k elements in table that's smaller than x
            total = 0
            for row in range(1, m + 1):
                qualify = min(x // row, n)
                if not qualify:
                    break
                total += qualify
            return total >= k

        lb, ub = 1, m * n
        while lb < ub:
            mid = lb + (ub - lb) // 2
            if enough(mid):
                # mid is feasible, explore smaller options (since problem as us to find smallest)
                ub = mid
            else:
                # mid is not feasible -> total less than k -> mid is too small
                lb = mid + 1
        return lb