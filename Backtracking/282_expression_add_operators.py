"""
128. Expression Add Operators
https://leetcode.com/problems/expression-add-operators/

Hard 
"""

# Questions: 
# 1. can we extract multiple consecutive digits at a time? i.e. '123' could be 12 + 3 or 1 + 23? 
# 2. should we return a list of strings? 
# 3. is the target always positive? 
# 4. what does it mean by expression should not contain leading zeros 
# 5. can we use built-in eval function? 
# Thoughts: 
# 1. sounds like a problem to enumerate all feasible solutions
# 2. can we try to use backtracking for it? 

def add_operators(num, target): 
	n, ans = len(num), []

	def backtrack(idx, prev, value, string): 
		if idx == n: 
			if value == target: 
				ans.append(string)
			return
		for i in range(idx + 1, n): 
			sub_str = num[idx:i]
			digits = int(sub_str)
			if len(digits) == 1 or digits[0] > 0:
				if prev is None:
					backtrack(i + 1, digits, digits, num[idx:i])
				else:
					backtrack(i + 1, digits, value + digits, string + '+' + sub_str)
					backtrack(i + 1, -digits, value - digits, string + '-' + sub_str)
					backtrack(i + 1, prev * digits, value - prev + prev * digits, string + '*' + sub_str)
		backtrack(0, None, 0, '')