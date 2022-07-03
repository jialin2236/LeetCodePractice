"""
140. Word Break II (Hard, 28 tagged)
https://leetcode.com/problems/word-break-ii/

given a string s and a list of strings wordDict.

add space in s to build a sentence where each word is a valid dict word. return all possible combination in any order
"""
from typing import List
# example
# s = 'pinapplepenallple", wordDict = ['apple', 'pen', 'applepen', 'pine', 'pineapple']
# -> ['pine apple pen apple', 'pineapple pen apple', 'pine applepen apple']

# we can use backtracking to constrcut all possibilities

# since a word could be reused multiple times
# convert wordDict to a set
# backtrack function input:
# i - index in s
# path - sentence constructed so far
# stopping criteria of backtrack:
# if i == len(s) -> append the path as a string to answer
# before i reaches len(s), backtracking logic
# we could take a substring from i to any j, where j >= i, as long as substring is in dictionary
# for j in range(i, len(s)):
# if s[i:j+1] in dictionary (if j == i, then it's a single letter word)
#    recursively call backtrack (j + 1, path + [s[i:j+1]])

class Solution:
    def word_break(self, s: str, word_dict: List[str]) -> List[str]:
        """
        m = len(s) and n = len(word_dict)
        time: i = 0, there are m possibilities, i = 1, m - 1, ... -> (m + (m-1) + ... + 1)
              -> ((m + 1) * m)/2 -> m^2
              in the worst case, every letter is s is in dict, alongside with combination.
              -> at every i, there are 2 possibilities 1) insert break 2) keep going -> O(2^m) times
              and takes O(n) to build the word set
              - > O(m^2 + 2^m + n)
        space: 2^m possible intermediate solutions for us to store, for each letter in s -> O(2^m*m)
               m^2
        :param s:
        :param word_dict:
        :return:
        """
        word_set = set(word_dict)
        ans = []

        def build_sentence(i: int, path: List[str]):
            if i == len(s):
                ans.append(' '.join(path))
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr in word_set:
                    build_sentence(j + 1, path + [substr])

        build_sentence(0, [])
        return ans