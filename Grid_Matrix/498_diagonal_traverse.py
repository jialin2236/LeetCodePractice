"""
498. Diagonal Traverse (Medium)
https://leetcode.com/problems/diagonal-traverse/

given
a m x n matrix mat
task
traverse elements in a diagonal order
output
list of ordered elements based on diagonal traversal

1   2   3
4   5   6   -> [1, 2, 4, 7, 5, 3. 6, 8, 9]
7   8   9      [00, 01, 10, 20, 11, 02, 12, 21, 22]

1   2   3   -> [1, 2, 4, 5, 3, 6]
4   5   6      [00, 01, 10, 11, 02, 12]
"""
from typing import List

# diagonal(mat)
# m, n = len(mat[0]), len(mat)
# ub = (m - 1) + (n - 1)
# pos_sum = [[] for _ in range(ub + 1)]
# for i in range(m):
#   for j in range(n):
#       pos_sum[i + j].append(mat[i][j])
# ans = []
# for idx, arr in enumearte(pos_sum):
#   if idx % 2: odd number
#       ans.extend(arr)
#   else:
#       ans.extend(arr[::-1])
# return ans

# diagonal(mat)
# ub = upper bound of (i + j), i, j being the 2D index
# for i in ranage(ub):
#   if i is even: head = (i, 0), d = (-1, 1)
#   if i is odd: head = (0, i), d = (1, -1)

class Solution:
    def diagonal_order1(self, mat: List[List[int]]) -> List[int]:
        """
        based on the sum of the 2D indices, if it's odd number, the initial index is (0, sum_ij) and direction
        is (1, -1), if it's even number, the initial index is (sum_ij, 0) and direction is (-1, 1)
        time: O(mn)
        space: O(1) - not counting the output
        :param mat:
        :return:
        """
        m, n = len(mat[0]), len(mat)
        ub = (m - 1) + (n - 1)
        ans = []
        for s in range(ub + 1):
            if s % 2:
                i = 0 if s < m else m - 1
                j = s if s < m else s - (m - 1)
                di, dj = 1, -1
            else:
                i = s if s < n else n - 1
                j = 0 if s < n else s - (n - 1)
                di, dj = -1, 1
            while 0 <= i < n and 0 <= j < m:
                ans.append(mat[i][j])
                i += di
                j += dj
        return ans

    def diagonal_order2(self, mat: List[List[int]]) -> List[int]:
        """
        traverse and store the diagonal from top to bottom, group by sum of the 2D index.
        when sum is even number, attach sublist in reverse order. when it's odd, attach sublist in order.
        time: O(mn)
        space: O(mn)
        :param mat:
        :return:
        """
        m, n = len(mat[0]), len(mat)
        ub = (m - 1) + (n - 1)
        idx_sum = [[] for _ in range(ub + 1)]
        for i in range(m):
            for j in range(n):
                idx_sum[i + j].append(mat[i][j])

        ans = []
        for idx, sub in enumerate(idx_sum):
            if idx % 2:
                # odd index sum
                ans.extend(sub)
            else:
                # even index sum
                ans.extend(sub[::-1])
        return ans