"""
766. Toeplitz Matrix (E)
"""
from typing import List
from collections import deque

# input m x n matrix, return true if the matrix is toeplitz
# every diagonal from top-left to bottom-right has the same elements

# we can traverse the matrix, and compare it with element[i-1][j-1] if exists

class Solution:
    def is_toeplitz(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if i -1 >= 0 and j - 1 >= 0:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True

# follow up
# if the matrix is stored on disk, and memory is limited ,
# such that you can only load at most one row of the matrix into the memory at once

class Followup:
    def is_toplitz(self, matrix: List[List[int]]):
        prev_r = deque(matrix[0])
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            row = matrix[i]
            prev_r.pop()
            prev_r.appendleft(row[0])
            for j in range(1, n):
                if row[j] != prev_r[j]:
                    return False
        return True 