"""
6. ZigZag Conversion
"""

# input - s: str, numRows: int
# output - str
# write s in zigzag pattern on numRows of rows. return its order line by line

# nr = numRows 
# nr = 1
# return of index: 01234...
# nr = 2
# 0 2 4 6
# 1 3 5 7
# 02461357 
# nr = 3
# 0   4   8
# 1 3 5 7 9
# 2   6   10
# 048135792610
# nr = 4
# 0     6 
# 1   5 7
# 2 4   8
# 3     9

class Solution: 
    def convert_nspace(self, s: str, numRows: int): 
        res = ['' for _ in range(numRows)]
        down = True
        row = 0
        for ele in s: 
            res[row] += ele
            row += 1 if down else -1
            if not 0 <= row < numRows:
                row += 2 if row < 0 else -2
                down = not down
        return ''.join(res)

    def convert_1space(self, s: str, numRows: int): 
        res = ''
        gap = 2 * numRows - 2
        if len(s) < numRows or numRows == 1: 
            return s
        for row in range(numRows): 
            g1 = 2 * (numRows - row - 1) if 0 < row < numRows - 1 else gap
            g2 = gap - g1 or gap
            i, g = row, True
            while i < len(s): 
                res += s[i]
                i += g1 if g else g2
                g = not g
        return res
