"""
670. Maximum Swap (Medium)
https://leetcode.com/problems/maximum-swap/

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

digits closer to the left (lower index), have a high priority
loop through the number
start from index 0
if there exist a digit in num[i + 1:] that is larger than num[i], swap and exit
larger than num[i] -> anything from num[i] to 9
"""


class Solution:
    def max_swap(self, num: int) -> int:
        # transform input to list
        nums = [int(i) for i in str(num)]
        # create a hash map to store index with value as key (like 2Sum)
        digit_idx = {val: idx for idx, val in enumerate(nums)}
        for i, v in enumerate(nums):
            for v_j in range(9, v, -1):
                # if there exist a value larger than current one, and is present in a later index
                # we swap
                if v_j in digit_idx and digit_idx[v_j] > i:
                    j = digit_idx[v_j]
                    nums[i], nums[j] = nums[j], nums[i]
                    # once we swap, since the problem only allows us to swap once, we exit
                    return int(''.join([str(i) for i in nums]))
        return int(''.join([str(i) for i in nums]))
