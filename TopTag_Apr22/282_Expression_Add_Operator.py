"""
282. Expression Add Operator
"""
from typing import List
# input s: str, target: int
# add operands in s to achieve target value, return all possible combinations, with no leading zero in the functions

# use backtracking (index, prev, path, value)
# base case
# if index == n: if value == target: add path to result
# iterative
# for j in range(i, n): if num[i] == 0 and j > 0 (trying to put together leading zero number), break
#                       curr = nums[i:j+1]
#                       add curr, call backtrack (j+1, int(curr), path + '+' + curr, value + int(curr))
#                       if i > 0, we can also try - and *, call backtrack as well

class Solution:
    def add_operators(self, num: str, target: int) -> List[str]:
        n = len(num)
        res = []

        def helper(i, prev, val, path):
            if i == n:
                if val == target:
                    res.append(path)
                return
            for j in range(i, n):
                if num[i] == 0 and j > i: break
                curr = num[i:j+1]
                helper(j + 1, int(curr), val + int(curr), path + '+' + curr)
                if i > 0:
                    helper(j + 1, -int(curr), val - int(curr), path + '-' + curr)
                    helper(j + 1, prev * int(curr), val - prev + prev * int(curr), path + '*' + curr)

        helper(0, 0, 0, '')
        return res