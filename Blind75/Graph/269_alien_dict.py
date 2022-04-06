"""
269. Alien Dictionary (Hard, 17 fb tagged 0-6 months)
https://leetcode.com/problems/alien-dictionary/

new alien language that uses the English alphabet, the order among letters is unknown.

given a list of strings (words) from the language dictionary, where the strings are sorted lexicographically by
this language's rule.

return a string of the unique letters sorted in lexicographically increasing order by new language's rules.
if no solution, return ''

a string s is lexicographically smaller than string t if at the first letter where they differ,
the letter in s comes before the letter in t in the alien language. If the s is a substr of t, s is smaller
if and only if s.length < t.length
"""
from typing import List
from collections import defaultdict, deque

# cases of s < t
# 1. "abc", "bcd"
# 2. "abc", "acd"
# 3. "abc", "abcd"

# from input words, we can build directed edges among letters
# use topological sorting to figure out the order of the new language

# building directed graph
# for i in in_word_index:
#   for j in words:
#       if (j, j + 1) has not been accounted for:
#           words_j,:i == words_j+1,:i
#           if words[j][i] != words[j+1][i]:
#               add edge to graph words[j][i] -> words[j+1][i] if edge not in graph
#               in_degree[words[j+1][i]] += 1 if edge not in graph
#               label (j, j+1) been accounted for
#           elif i == end of words[j] and words[j][i] == words[j+1][i]: label (j, j + 1) been accounted for
#       if all (j, j+ 1) has been accounted for (with n_words - 1 elements): break the loop

# use topolotical sorting on directed graph
# add letters with 0 in degree into initial queue
# use bfs on queue
# while queue not empty:
#       pop top element
#       for suffix nodes of top element:
#           decrement node's in degree
#           if node's in degree == 0: add node to queue

class Solution:
    def alien_order(self, words: List[str]) -> str:
        """
        time: O(sum([len(w) for w in words])) for building graph and in_degree, O(E) for topolotical sort -> at most
              O(N - 1) -> total time complexity = O(sum(len_of_each_word))
        space: graph = O(n_letters + E) = O(n_letters + min(N, n_letters^2)), in_degree = O(n_letters), queue = O(n_letters)
               -> O(1) since number of edges has a max value at 26^2
        :param words:
        :return:
        """
        graph = defaultdict(set)
        n_words, n_chars = len(words), max([len(w) for w in words])
        in_degree = {char: 0 for word in words for char in word}
        counted = set()
        for i in range(n_chars):
            for j in range(n_words - 1):
                if (j, j + 1) not in counted:
                    if i < len(words[j]) and i < len(words[j + 1]) and words[j][i] != words[j + 1][i]:
                        if words[j + 1][i] not in graph[words[j][i]]:
                            graph[words[j][i]].add(words[j + 1][i])
                            in_degree[words[j + 1][i]] += 1
                        counted.add((j, j + 1))
                    elif i == len(words[j]) - 1 and words[j][i] == words[j + 1][i]:
                        counted.add((j, j + 1))
                if len(counted) == n_words - 1:
                    break

        queue = deque([char for char, id in in_degree.items() if id == 0])
        ans = []
        while queue:
            top = queue.popleft()
            ans.append(top)
            for nei in graph[top]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return ''.join(ans) if len(ans) == len(in_degree) else ''
