"""
249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/

Medium
"""
# Questions:
# 1. do the same sequence required to have the same length? 
# 2. what is the successive letter of 'z'? if it's 'a', would 'az' but the same seq as 'ba'? 
# 3. for 2 words to be of same pattern, can we say the list with number of 
# 	 gaps between each neighboring character is the same?
# 4. for a string with 5 character, it's sequence = [gap_0, gap_1, gap_2, gap_3] 
# 	 where gap_i = ord(s[i+1]) - ord(s[i]) if positive else 26 + gap 
# 5. could the string the empty?
import collections
from collections import defaultdict
from typing import List


class Solution:
	def group_string(self, strings: List[str]) -> List[List[str]]:
		def str2base(s: str) -> str:
			res = []
			base = ord(s[0])
			for ch in s[1:]:
				d2b = ord(ch) - base
				adj_d2b = d2b if d2b >= 0 else (26 + d2b)
				res.append(chr(adj_d2b + ord('a')))
			return ''.join(res)

		seq_hash = defaultdict(list)
		for string in strings:
			base_string = str2base(string)
			seq_hash[base_string].append(string)
		return [grp for grp in seq_hash.values()]
