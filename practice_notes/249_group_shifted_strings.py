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
from collections import defaultdict


class Solution: 
	def get_pattern(s): 
		if len(s) == 1: 
			return (None, 1)
		if not s:
			return (None, 0)
		else: 
			sqn = []
			for i in range(len(s) - 1):
				diff = ord(s[i+1]) - ord(s[i])
				diff = diff + 26 if diff < 0 else diff
				sqn.append(diff)
			return (sqn, len(s))


	def group_str(strings): 
		# use a hash map to store all sequence, and their qualifying strings
		sequence = defaultdict(list)
		for string in strings:
			str_pattern = self.get_pattern(string)
			sequence[str_pattern].append(string)
		return [i for i in sequence.items()]