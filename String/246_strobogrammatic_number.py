"""
246. Strobogrammatic Number (Easy, 20 tagged)
https://leetcode.com/problems/strobogrammatic-number/

given num: str, which is an int. return if num is a strobogrammatic number
note: a strobogrammatic number is a number that looks the same when rotated 180 degrees
"""

# example
# 69 -> true, 88 -> true, 962 -> false

# Approach
# when numbers rotated 180:
# hash_table = {0: 0, 1 -> 1, 6: 9, 8: 8, 9: 6}
# use 2 pointers from both ends of the string
# if one of the number is not in hash_table: return false
# if hash[left] = right, increment/decrement
# else: return false

class Solution:
    def is_strobogrammatic(self, num: str) -> bool:
        lookup = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        i, j = 0, len(num) - 1
        while i <= j:
            if not (num[i] in lookup and num[j] in lookup):
                return False
            if lookup[num[i]] != num[j]:
                return False
            else:
                i += 1
                j -= 1
        return True 