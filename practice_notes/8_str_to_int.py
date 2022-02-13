class Solution(object):
    def myAtoi(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        positive = False if s[0] == '-' else True
        s = s[1:] if s[0] in ['-', '+'] else s
        lb, ub = -2**31, 2**31 - 1
        i, sums, m = 0, 0, 10
        n = 1 if positive else -1
        while i < len(s) and s[i].isnumeric() and lb <= sums <= ub:
            sums = sums*m + int(s[i])*n
            i += 1
        if sums < lb or sums > ub:
            sums = ub if positive else lb
        return sums


if __name__ == '__main__':
    solution = Solution()
    test_c = "   -42"
    print(solution.myAtoi(test_c))