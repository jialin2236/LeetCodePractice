"""
202. happy number
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        def ss(num: int) -> int:
            ss = 0
            while num > 0:
                num, d0 = divmod(num, 10)
                ss += d0 ** 2
            return ss

        # approach 1
        # hashmap = set()
        # while n != 1 and n not in hashmap:
        #     hashmap.add(n)
        #     n = ss(n)
        # return n == 1

        # approach 2
        slow = n
        fast = ss(n)
        while fast != 1 and fast != slow:
            slow = ss(slow)
            fast = ss(ss(fast))
        return fast == 1

