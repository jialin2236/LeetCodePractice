"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""

"""
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Input: n = 0
Output: 0

Input: n = 1
Output: 0
"""

from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        numbers = set()
        for p in range(2, int(sqrt(n))+1):
            if p not in numbers:
                for multiples in range(p*p, n, p):
                    numbers.add(multiples)

        return n - len(numbers) - 2