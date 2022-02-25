"""
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Medium
"""

"""
a parentheses string is valid if and only if: 
- it's empty
- it can be written as AB, where A and B are valid string
- It can be written as (A), where A is a valid string

given a parentheses string s. In one move, you can insert a parenthesis
at any position of the string. 
Return the min number of moves required to make s valid. 
"""
# idea
# can we have a variable n_open to keep track of open parentheses
# ans = 0 
# example: "))(((" or "((())))"
# when encounter a closed parenthesis, check n_open
# if n_open > 0 -> we have encountered some '(' to complement this ')'
# n_open -= 1
# if n_open == 0 -> have not seen enough '(' to complement this ')'
# ans += 1
# at the end, return ans + n_open 

def minAddToMakeValid(s: str) -> int:
	add_close, add_open = 0, 0
	for c in s: 
		if c == '(': 
			add_close += 1
		if c == ')':
			if add_close:
				add_close -= 1
			else: 
				add_open += 1
	return add_close + add_open 