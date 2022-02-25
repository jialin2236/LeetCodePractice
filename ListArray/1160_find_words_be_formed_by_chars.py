"""
1160. Find Words That Can Be Formed by Characters

You are given an array of strings [words] and a string 'chars'.

A string in [word] is good if it can be formed by characters from 'chars' (each character can only be used once).

Return the sum of lengths of all good strings in words.

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""
from typing import List, Dict

class Solution:
    def count_words(self, words: List[str], chars: str) -> int:
        def qualifies(chars: str, hash_map: Dict) -> bool:
            for c in chars:
                if c not in hash_map or hash_map[c] == 0:
                    return False
                hash_map[c] -= 1
            return True

        ans = 0
        chars_hash = {}
        for ci in chars:
            if ci not in chars_hash:
                chars_hash[ci] = 0
            chars_hash[ci] += 1

        for word in words:
            if qualifies(word, chars_hash): 
                ans += len(word)
        return ans



