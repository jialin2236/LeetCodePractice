"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List


# 1
# create a lookup function
# loop through input string and create all possible combination
class Solution:
    def __init__(self):
        self.lookup = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
              "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def combo_recursive(self, digits: str) -> List[str]:
        def backtrack(index, combo_i):
            if len(combo_i) == len(digits):
                combo.append("".join(combo_i))
                return
            letters = self.lookup[digits[index]]
            for letter in letters:
                combo_i.append(letter)
                backtrack(index + 1, combo_i)
                combo_i.pop()

        combo = []
        backtrack(0, [])
        return combo

