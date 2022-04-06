"""
415. Add Strings (Easy, 45 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/add-strings/

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.
"""

# since we cannot directly convert the inputs into integers, we will need to do it one digit by one digit
# use the concept of addition

def add_strings(num1: str, num2: str) -> str:
    ans = []
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    while i >= 0 or j >= 0:
        n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
        n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
        carry, digit = divmod(n1 + n2 + carry, 10)
        ans.append(str(digit))
        i -= 1
        j -= 1
    return ''.join(ans[::-1])