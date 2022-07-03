"""
415. Add Strings (E)
"""

# given 2 strings of numbers, return the sum of the 2 numbers in string
# cannot convert input into int

class Solution:
    def add_string(self, num1: str, num2: str) -> str:
        # start from the end
        i, j, carry = len(num1)-1, len(num2)-1, 0
        arr = []
        while i >= 0 and j >= 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            carry, val = divmod(n1 + n2 + carry, 10)
            arr.append(str(val))
        if carry:
            arr.append(str(carry))
        return ''.join(arr[::-1])