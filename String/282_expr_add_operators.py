"""
282. Expression Add Operators (Hard, 23 fb tagged 0 ~ 6 months)

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary
operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.
"""
from typing import List

# we're only allow to insert operators ['+', '-', '*']
# since operator effects could be canceled out later on using each other, we cannot have a strict mid process
# stopping criteria
# can we use backtracking?
# Backtracking(idx, partial_solution) -> None: (add qualified solutions to answer array)
# if idx == len(input) and str2int(partial_solution) == target: ans.append(partial_solution) return
# for option in options (not add anything, add +, add -, add *):
#   append option to partial_solution
#   recursively call backtracking (idx + 1, partial_soulution) for if we don't add anything
#   recursively call backtracking (idx, partial_soulution) for if we added operator
#   partial_solution.pop()

class Solution:
    def addOperators_clean(self, s: str, target: int) -> List[str]:
        """
        time: O(N*4^N) - there are 4 options at every step, and we go through N of them, and at worst each time we could
              have N operations to calculate
        space: O(
        :param s:
        :param target:
        :return:
        """
        def backtrack(i, path, resultSoFar, prevNum):
            if i == len(s):
                if resultSoFar == target:
                    ans.append(path)
                return

            for j in range(i, len(s)):
                if j > i and s[i] == '0': break  # Skip leading zero number
                num = int(s[i:j + 1])
                if i == 0:
                    backtrack(j + 1, path + str(num), resultSoFar + num, num)  # First num, pick it without adding any operator
                else:
                    backtrack(j + 1, path + "+" + str(num), resultSoFar + num, num)
                    backtrack(j + 1, path + "-" + str(num), resultSoFar - num, -num)
                    backtrack(j + 1, path + "*" + str(num), resultSoFar - prevNum + prevNum * num, prevNum * num)  # Can imagine with example: 1+2*3*4

        ans = []
        backtrack(0, "", 0, 0)
        return ans
