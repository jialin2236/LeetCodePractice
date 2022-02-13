"""
79. Word Search
https://leetcode.com/problems/word-search/

Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

"""
input: board List[List[str]], word: str
output: bool

1. the longest word the board could represent, is (2m + 2n) where dim(board) = m by n
2. can we use backtrack idea? 

when we reach the end of word, return true
board_idx, word_idx, visited
for idx in neighbor
    if idx not been visited & board[idx] == word[word_idx]]: 
        visited.add(idx)
        explore(idx, word_idx + 1, visited)
"""
from typing import List


class Solution:
    def find_neighbors(self, idx: List[int], m: int, n: int) -> List[List[int]]:
        row, col = idx
        neigh = []
        if col > 0:
            neigh.append([row, col - 1])
        if col < n - 1:
            neigh.append([row, col + 1])
        if row > 0:
            neigh.append([row - 1, col])
        if row < m - 1:
            neigh.append([row + 1, col])
        return neigh

    def word_search(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        word_len = len(word)
        if word_len >= 2 * (m + n):
            return False
        def steps_till_end(prev: List[int], curr: List[int]) -> int:
            prev_r, prev_c = prev
            curr_r, curr_c = curr
            r_gap, c_gap = prev_r - curr_r, prev_c - curr_c
            if not c_gap:
                r_step = m - curr_c - 1 if c_gap else curr_c
                c_step = curr_c if curr_c > n // 2 else n - curr_c
            else:
                c_step = n - curr_r - 1 if r_gap else curr_r
                r_step = curr_r if curr_r > m//2 else m - curr_r
            return c_step + r_step + (m + n)

        def backtrack(board_idx, word_idx, visited):
            if word_idx == word_len:
                return True
            neigh_idx = self.find_neighbors(board_idx, m, n)
            for i, j in neigh_idx:
                if [i, j] not in visited and steps_till_end(board_idx, [i, j]) >= word_len - (word_idx + 1):
                    if board[i][j] == word[word_idx]:
                        visited.add([i, j])
                        backtrack([i, j], word_idx + 1, visited)
                        visited.remove([i, j])

        v = set()
        b = backtrack([0, 0], 0, v)
        ans = False if not b else True
        return ans
