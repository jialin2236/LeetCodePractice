"""
65. Valid Number
Hard

A valid number can be split up into these components (in order):
1. A decimal number or an integer.
2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One of the following formats:
    1. One or more digits, followed by a dot '.'.
    2. One or more digits, followed by a dot '.', followed by one or more digits.
    3. A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
1. (Optional) A sign character (either '+' or '-').
2. One or more digits.

For example, all the following are valid numbers:
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7",
"+6e-1", "53.5e93", "-123.456e789"],
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
"""


class Solution:
    def isInteger(self, s: str) -> bool:
        if not (s[0].isdigit() or s[0] in ['+', '-']):
            return False
        for i in range(1, len(s)):
            if not s[i].isdigit():
                return False
        return True

    def isDecimal(self, s: str) -> bool:
        point = False
        if s[0] == '.':
            point = True
        elif not (s[0].isdigit() or s[0] in ['+', '-']):
            return False
        for i in range(1, len(s)):
            if s[i] == '.':
                if point:
                    return False
                else:
                    point = True
            else:
                if not s[i].isdigit():
                    return False
        return point

    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        if self.isInteger(s) or self.isDecimal(s):
            return True
        else:
            if not (s[0].isdigit() or s[0] in ['+', '-']):
                return False
            for i in range(1, len(s)):
                if s[i].lower() == 'e':
                    p1 = self.isDecimal(s[:i]) or self.isInteger(s[:i])
                    p2 = self.isInteger(s[i+1:])
                    return p1 and p2
            return False

    def validNumber(self, s: str) -> bool:
        seen_e = False
        seen_dot = False
        seen_sign = False
        seen_digit = False
        for si in s:
            if si.lower() == 'e':
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_sign = False
                seen_digit = False
            elif si in ['+', '-']:
                if seen_sign or seen_digit:
                    return False
                seen_sign = True
            elif si == '.':
                if seen_dot or seen_e:
                    return False
            elif si.isdigit():
                seen_digit = True
        return seen_digit
