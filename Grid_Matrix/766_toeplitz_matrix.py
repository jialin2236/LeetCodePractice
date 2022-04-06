"""
766. Toeplitz Matrix (Easy, 31 fb tagged 0~6 months)
https://leetcode.com/problems/toeplitz-matrix/

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
"""
from typing import List

# example
# [[1,2,3,4], [5,1,2,3], [9,5,1,2]]
# true

# given index i, j
# diagonal neighbors: (i + 1, j + 1), (i - 1, j - 1)

class isToeplitzMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.m, self.n = len(matrix) - 1, len(matrix[0]) - 1

    def hash_table(self):
        group = {}
        for r, row in enumerate(self.mat):
            for c, val in enumerate(row):
                if r - c not in group:
                    group[r - c] = val
                elif val != group[r - c]:
                    return False
        return True

    def two_loop(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.mat[i][j] != self.mat[i + 1][j + 1]:
                    return False
        return True

    def one_line(self):
        return all(r1[:-1] == r2[1:] for r1, r2 in zip(self.mat, self.mat[1:]))

    def is_toeplitz_matrix(self) -> bool:
        diag_i, diag_j = self.m - 1, 0
        while diag_i >= 0 and diag_j <= self.n - 1:
            diag_val = self.mat[diag_i][diag_j]
            ni, nj = diag_i + 1, diag_j + 1
            while ni <= self.m and nj <= self.n:
                if self.mat[ni][nj] != diag_val:
                    return False
                ni += 1
                nj += 1
            diag_j = 0 if diag_i > 0 else diag_j + 1
            diag_i = diag_i - 1 if diag_i > 0 else 0
        return True
