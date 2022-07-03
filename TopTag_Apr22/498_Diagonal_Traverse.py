"""
498. Diagonal Traverse (M, 43)
"""
from typing import List

# given an m x n matrix mat, return an array of all elements of the array in a diagonal order
# order goes, diagonal first, when reached boundary -> anti diagonal next
# 1 2 3
# 4 5 6
# 7 8 9
# -> [1,2,4,7,5,3,6,8,9]

class Solution:
    def find_diagonal_order(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        # there are 2 diagonal directions
        d, ad = (-1, 1), (1, -1)
        i, j, res = 0, 0, []
        curr_d = d
        while i + j <= m + n - 2:
            while 0 <= i < m and 0 <= j < n:
                # all entries are inbound
                res.append(mat[i][j])
                i += curr_d[0]
                j += curr_d[1]
            # gets out of bound
            if curr_d == d:
                # if direction is (-1, 1)
                # j can only increment, i can only decrement
                # if j goes out of bound, j >= n, i goes out of bound, i < 0
                # 1. j is out of bound
                if j >= n:
                    j -= 1
                    i += 2
                # 2. j is in bound
                else:
                    i += 1
                # switch direction
                curr_d = ad
            else:
                # if direction is (1, -1)
                # i can only increment, j can only decrement
                # if i is out of bound, guarantee i >= m
                # if j is out of bound, guarantee j < 0
                if i >= m:
                    i -= 1
                    j += 2
                else:
                    j += 1
                # switch direction
                curr_d = d
        return res