"""
289. Game of Life
https://leetcode.com/problems/game-of-life/
Medium
"""

"""
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""

"""
modify in place, for each cell board[i][j], to determine its next state, we need: 
1. board[i][j-1], board[i][j+1]
2. board[i-1][j-1], board[i-1][j], board[i-1][j+1]
3. board[i+1][j-1], board[i+1][j], board[i+1][j+1]

can we record the value of the original prev_row, and prev_ele before inplace modifying it? so: 
seen = [board[i-1], board[i][j-1]]
unseen = [board[i][j+1], board[i+1]]

as we traverse through the board, pop the first and last element in seen, append the current element
prior to modifying it. 
useful_seen = 
[0-2, -1] for middle elements
[0,1] for left boundary
[0,-1] for right boundary
"""
from typing import List

class Solution:
    def game_of_life(self, board: List[List[int]]) -> None:
        stack = []
        m, n = len(board), len(board[0])
        i = 0
        while i < m:
            j = 0
            prev_ele = 0
            while j < n:
                prev_row = stack.pop() if i > 0 else 0
                next_ele = board[i][j+1] if j < n - 1 else 0
                next_row = board[i+1][j] if i < m - 1 else 0
                next_row += board[i+1][j-1] if (i < m - 1 and j) else 0
                next_row += board[i+1][j+1] if (i < m - 1 and j < n-1) else 0
                neigh = prev_row + prev_ele + next_ele + next_row
                stack_a = prev_ele + next_ele + board[i][j]
                prev_ele = board[i][j]
                if board[i][j] == 1:
                    if neigh < 2 or neigh > 3:
                        board[i][j] = 0
                else:
                    if neigh == 3:
                        board[i][j] = 1
                stack.append(stack_a)


