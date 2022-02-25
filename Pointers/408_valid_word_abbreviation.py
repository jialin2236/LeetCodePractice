"""
408. Valid Word Abbreviation 
https://leetcode.com/problems/valid-word-abbreviation/

Easy
"""

"""
a string can be abbreviated by replacing any number of non-adjacent, 
non-empty substrings with their lengths. The lengths should not have 
leading zeros.

for example, "substitution" -> "s10n", "sub4u4", "12", "su3ilu2on", 
"substitution" (no substring replaced)

not valid: 
"s55n" replaced substrings are adjacent
"s010n" has leading zeros
"s0ubstitution" replaces an empty substring

Given a string word and an abbreviation abbr, return whether the string 
matches the given abbreviation.
"""

# loop through abbr using a pointer i
# if abbr[i].isalpha(), check if abbr[i] == word[i]
# else (is number), if it's the 1st number idx and abbr[i] == '0' -> return False
# else (first number and not 0), search for sequence (i:j) increment i by abbr[i:j]
# 
# Time: O(N), Space: O(1)
def valid_abbr(word: str, abbr: str) -> bool: 
	i, j, n = 0, len(word)
	while i < n: 
		if abbr[j].isalpha:
			if abbr[j] != word[i]:
				return False
			i += 1
			j += 1
		elif (j and abbr[j-1].isalpha()) or (j == 0): # first digit of a sequence
			if abbr[j] == 0: 
				return False
			else: 
				k = j + 1
				while k < n and abbr[j].isdigit():
					k += 1
				j = k
				i += int(abbr[i:k])
				if i >= n: 
					return False
	return True


