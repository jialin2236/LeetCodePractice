"""
670. Maximum Swap (M, 29)
"""

# given an integer num
# can swap 2 digits at most once to get the max valued number
# return max valued number you can get

class Solution:
    def max_swap(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        n = len(num)
        max_i = n - 1
        i, j = 0, 0
        for idx in range(n-1, -1, -1):
            if num[idx] > num[max_i]:
                max_i = idx
            elif num[idx] < num[max_i]:
                i = idx
                j = max_i
        num[i], num[j] = num[j], num[i]
        return int(''.join([str(x) for x in num]))

    def max_swap1(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        idx = {val: i for i, val in enumerate(num)}
        n = len(num)
        for i in range(n):
            for a in range(9, num[i], -1):
                if a in idx and idx[a] > i:
                    num[i], num[idx[a]] = num[idx[a]], num[i]
                    return int(''.join([str(x) for x in num]))
        return int(''.join([str(x) for x in num]))