"""
54. Spiral Matrix
"""
from typing import List

# input matrix: List[List[int]]
# output List[int] - traverse input matrix in spiral order

class Solution: 
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        m, n = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, m, 0, n
        res = [matrix[0][0]]
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y , i = 0, 0, 0
        while len(res) < m * n:
            dx, dy = d[i % 4]
            while top <= x + dx < bottom and left <= y + dy < right: 
                x += dx
                y += dy
                res.append(matrix[x][y])
            i += 1
            if dy: 
                if dy > 0:
                    top += 1
                else: 
                    bottom -= 1
            else: 
                if dx > 0: 
                    right -= 1
                else: 
                    left += 1
        return res