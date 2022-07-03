"""
311. Sparse Matrix Multiplication (M)
"""
from typing import List, DefaultDict
from collections import defaultdict
# given 2 sparse matrix, of size m x k and k x m, return mat1 x mat2

# knowing m1 is of dimension m x k, m2 of dimension k x n
# m1 x m2 has dimension m x n
# m = m1 x m2
# m[r][c] = sum(m1[r][i] x m2[i][c]) over all i

class Solution:
    def multiply(self, m1: List[List[int]], m2: List[List[int]]) -> List[List[int]]:
        # we can condense the matrix first
        def condense(mat: List[List[int]]) -> DefaultDict:
            res = defaultdict(list)
            rows, cols = len(mat), len(mat[0])
            for r in range(rows):
                for c in range(cols):
                    if mat[r][c]:
                        res[r].append(c)
            return res

        m, n = len(m1), len(m2[0])
        mc1, mc2 = condense(m1), condense(m2)
        ans = [[0 for i in range(n)] for j in range(m)]
        for row1 in mc1:
            for col1 in mc1[row1]:
                if col1 in mc2:
                    for col2 in mc2[col1]:
                        ans[row1][col2] += m1[row1][col1] * m2[col1][col2]
        return ans