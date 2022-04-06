"""
227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

Medium
"""

# Questions: 
# 1. are all numeric characters integers? could there be decimal points? 
# 2. are there parenthese? i.e. (3+2)*3? 
# 3. is [+, - , *, /] the only operations?
# 4. any requirement on space usage? 
# 5. could the string start with a sign, say +/-? 
# 6. could 2 signs appear consecutively? say 6+-5, or 6*-5? 

# let's work with an example: "4-3+2*4/5"
# we can separate the string by +/-
# traverse through the string
# use ans to track the final answer, curr to track the result of the current part
# at the start, until we see the first +/-: 
# 1. if the char is numeric, add it to curr
# 2. if the char is [*,/], scan string after char till we see the next non-numeric char
# 3. curr [+,/]= number till next non-numeric char
# as soon as we see the next +/-
# 4. add curr to ans, reset curr to 0
# 5. repeat 1 - 3
# 6. if +/- from step 3 is -, subtract curr from ans, reset curr to 0

def basic_calculator(s: str) -> int: 
	ans, curr, plus = 0, 0, True
	idx = 0 
	while idx < len(s):
		ch = s[idx]
		if ch.isnumeric():
			curr = curr * 10 + int(ch)
			idx += 1
		if ch in ['+', '-']:
			ans += curr if plus else (-curr)
			curr, plus = 0, True if ch == '+' else False
			idx += 1
		if ch in ['*', '/']:
			post = 0
			while idx + 1 < len(s) and s[idx + 1].isnumeric(): 
				post = post * 10 + int(s[idx + 1])
				idx += 1
			curr = curr * post if ch == '*' else curr // post
	ans += curr if plus else (-curr)
	return ans 

