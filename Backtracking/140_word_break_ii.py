"""
140. Word Break II
https://leetcode.com/problems/word-break-ii/
Hard

Given a string s and a dictionary of strings wordDict,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

"""
from typing import List


# backtrack(candidate)
# if is_solution(candidate):
#      output(candidate)
#      return
# for next_candidate in list_of_candidates:
#       if is_feasible(next_candidate):
#              add(next_candidate)
#              backtrack(next_candidate)
#              remove(next_candidate)
class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> List[str]:
        ans, n = [], len(s)
        word_set = set(word_dict)

        def backtrack(idx, sentence):
            if idx == n:
                ans.append(' '.join(sentence))
                return
            for j in range(idx + 1, n):
                word = s[idx:j+1]
                if word in word_set:
                    sentence.append(word)
                    backtrack(j + 1, sentence)
                    sentence.pop()

        backtrack(0, [])
        return ans