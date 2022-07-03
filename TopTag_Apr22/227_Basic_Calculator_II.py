"""
227. Basic Calculator II (M, 115)
"""

# given a string of an expression
# return its value
# division to truncate to zero

# Approach
# variables needed
# 1. curr: int to indicate current value
# 2. positive: bool to indicate sign of current value
# scenarios
# 1. we should separate (if we could) the string into parts with +/- signs
# 2. calculation within each part should be independent
# 3. when we see the next +/-, it's an indication of adding curr to total

# loop through the string s
# curr = 0, positive = True, total = 0
# i = 0, while i < len(s)
# if s[i] in ['+', '-'] -> total += curr if positive else (-curr), curr = 0, positive = True if s[i] == '+' else False
# if s[i].isdigit() -> curr = 10 * curr + s[i]
# if s[i] in ['*', '/'] -> i = i + 1, mul = 0, while s[i].isdigit(): mul = mul * 10 + s[i], i += 1
# curr = curr * mul if s[i] == '*' else int(curr/mul)
# after exiting the loop: total += curr to add the final part to the total

class Solution:
    def calculate(self, s: str) -> int:
        total = curr = 0
        positive = True
        i = 0
        while i < len(s):
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])
            elif s[i] in ["+", "-"]:
                total += curr if positive else (-curr)
                curr = 0
                positive = True if s[i] == "+" else False
            elif s[i] in ["*", "/"]:
                m = True if s[i] == '*' else False
                i += 1
                mul = 0
                while i < len(s) and (s[i].isdigit() or s[i] == " "):
                    if s[i].isdigit():
                        mul = mul * 10 + int(s[i])
                    i += 1
                curr = curr * mul if m else int(curr / mul)
                continue
            i += 1
        total += curr if positive else (-curr)
        return total

    def calculate_stack(self, s: str) -> int:
        prev_op = "+"
        curr = ""
        stack = []
        for char in s + '+':
            if char.isdigit():
                curr += char
            elif char in '+-*/':
                if prev_op == '+':
                    stack.append(int(curr))
                elif prev_op == '-':
                    stack.append(-int(curr))
                elif prev_op == '*':
                    prev_num = stack.pop()
                    stack.append(prev_num * int(curr))
                else:
                    prev_num = stack.pop()
                    stack.append(prev_num // int(curr))
                prev_op = char
                curr = ""

        return sum(stack)