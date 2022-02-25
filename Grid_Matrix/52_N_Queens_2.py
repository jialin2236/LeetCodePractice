"""
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""


class Solution:
    def parent_func(self, n: int) -> int:
        queen = [[False] * n for _ in range(n)]
        col_attack_zone = set()
        diag_attack_zone = set()
        anti_diag_attack_zone = set()

        def place_queen(row, col):
            queen[row][col] = True
            # update attack zone
            col_attack_zone.add(col)
            diag_attack_zone.add(row + col)
            anti_diag_attack_zone.add(row - col)

        def remove_queen(row, col):
            queen[row][col] = False
            col_attack_zone.remove(col)
            diag_attack_zone.remove(row + col)
            anti_diag_attack_zone.remove(row - col)

        def backtrack(row) -> int:
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col not in col_attack_zone \
                        and (row + col) not in diag_attack_zone \
                        and (row - col) not in anti_diag_attack_zone:
                    place_queen(row, col)
                    count += backtrack(row + 1)
                    remove_queen(row, col)
            return count
        return backtrack(0)