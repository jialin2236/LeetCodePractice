"""
408. Valid Word Abbreviation (E, 108)
"""

# what we know
# a string can be abbreviated by replace any number of non-adjacent, non-empty strings with their lengths
# length has no leading zeros

# no leading zero
# no adjacent replacement
# no empty substring replacement

# Approach
# traverse the word
# outer and inner loop
# outer loop: if we encounter a digit, and the digit is zero -> false
#           inner loop: triggered when encounters a non-zero digit in outter loop
#                     while s[index] is digit, count it to the index increments
#           increment the index
#           if index > len(loop) -> false

class Solution:
    def valid_word_abbr(self, word: str, abbr: str) -> bool:
        """
        time: O(n) - n is the length of abbr
        space: O(1)
        :param word:
        :param abbr:
        :return:
        """
        i, j = 0, 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isalpha():
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[i] == '0':
                    return False
                idx = 0
                while i < len(abbr) and abbr[i].isdigit():
                    idx = 10 * idx + int(abbr[i])
                    i += 1
                j += idx
        return j == len(word) and i == len(abbr)