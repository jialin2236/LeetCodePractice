"""
30. Substring with Concatenation of All Words
Hard

You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once,
in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
"""
from typing import List
from collections import Counter, defaultdict


# find k: length of word in words
# find goal substr length: k * n, where n is size of words
# extend right when substring is less than k * n
# check match once substring reach k * n
# retract left by k once substring reach right size and checked match
# stop when left reaches end of s minus k * n
class Solution:
    def substr_concat_words(self, s: str, words: List[str]) -> List[int]:
        k, n_words, n_str = len(words[0]), len(words), len(s)
        substr_size = k * n_words
        words_counter, substr_counter = Counter(words), Counter()
        ans = []
        left = 0
        while left < n_str - substr_size:
            i = left
            while s[i:i + k] in substr_counter:
                i += k
            j = i + k
            while j - left + 1 <= substr_size:
                s_ij = s[i:j]
                if s_ij in words_counter:
                    substr_counter[s_ij] += 1
                    i = j
                    j += k
                else:
                    substr_counter = Counter()
                    break
            if substr_counter == words_counter:
                ans.append(left)
                rmv_word = s[left:left+k]
                substr_counter[rmv_word] -= 1
                if not substr_counter[rmv_word]:
                    del substr_counter[rmv_word]
                left += k
            else:
                left = i
        return ans


class Solution_std:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = Counter(words)

        def sliding_window(left):
            words_found = defaultdict(int)
            words_used = 0
            excess_word = False

            # Do the same iteration pattern as the previous approach - iterate
            # word_length at a time, and at each iteration we focus on one word
            for right in range(left, n, word_length):
                if right + word_length > n:
                    break

                sub = s[right : right + word_length]
                if sub not in word_count:
                    # Mismatched word - reset the window
                    words_found = defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length # Retry at the next index
                else:
                    # If we reached max window size or have an excess word
                    while right - left == substring_size or excess_word:
                        # Move the left bound over continously
                        leftmost_word = s[left : left + word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1

                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            # This word was the excess word
                            excess_word = False
                        else:
                            # Otherwise we actually needed it
                            words_used -= 1

                    # Keep track of how many times this word occurs in the window
                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        # Found too many instances already
                        excess_word = True

                    if words_used == k and not excess_word:
                        # Found a valid substring
                        answer.append(left)

        answer = []
        for i in range(word_length):
            sliding_window(i)

        return answer