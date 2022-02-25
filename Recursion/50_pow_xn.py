class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -1*n
            x = 1/x
        return self.pow(x, n)

    def pow(self, x, n):
        if n == 0:
            return 1
        mid = self.pow(x, n//2)
        if n % 2 == 0:
            return mid * mid
        return mid * mid * x


if __name__ == '__main__':
    solve = Solution()
    print(solve.myPow(4, -2))
