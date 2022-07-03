"""
1539. Kth Missing Positive NUmber (E/M, 28 tagged)
https://leetcode.com/problems/kth-missing-positive-number/

given an arr: List[int] if all positive numbers, sorted in a strictly increasing order, and k: int

find the kth positive integer that is missing from array
"""
from typing import List

# example
# arr = [2,3,4,7,11], k = 5
# output: 9
# missing numbers are [1,5,6,8,9,10,...], the 5th missing positive integer is 9

# Approach 1
# we can find number of missing ints from before arr[0], after arr[-1] and between arr
# missing_before_arr_start = arr[0] - 1
# missing_before_arr_end = arr[-1] - len(arr)
# missing_between = arr[-1] - len(arr) - missing_before
# missing_after = from arr[-1] to inf (?)

# if k > missing_before_arr_end:
# for example, k = 5, arr = [2,3,4,7], missing_before_arr_end = 7 - len(arr) = 3 ([1,5,6])
# ans = k - missing_before_arr_end + arr[-1] = 5 - 3 + 7 = 9 ([1,5,6,8,9,10,...])

# if k <= missing_before_arr_start:
# for example, k = 2, arr = [4,5,6,9],
# missing_before_arr_end = 9 - len(arr) = 5 ([1,2,3,7,8])
# missing_before_arr_start = arr[0] - 1 = 3 ([1,2,3])
# ans = k

# if missing_before_start < k <= missing_before_arr_end:
# we can find our answer in missing number inside the arr
# since arr is sorted, we can use binary search
# left, right = 0, len(arr) - 1
# goal: find (k - missing_before_arr_start)th missing inside arr
# example: arr = [2,3,4,7,11], k = 5
# missing_before_arr_start = 1, missing_before_arr_end = 11 - 5 = 6
# -> we need to find k' = (k - 1) = 4th missing int in arr
# [1,5,6,8,9,10,...]
# while left < right:
#   mid = (left + right) // 2
#   if missing before mid > k': search on first half
#   else (missing before mid < k'): k' -= missing_before_mid, search on second half

class Solution:
    def find_kth_positive(self, arr: List[int], k: int) -> int:
        missing_before_arr_start, missing_before_arr_end = arr[0] - 1, arr[-1] - len(arr)
        if k <= missing_before_arr_start:
            return k
        if k > missing_before_arr_end:
            return k - missing_before_arr_end + arr[-1]
        # answer is within arr
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right + 1) // 2
            missing_before_mid = arr[mid] - (mid + 1)
            if missing_before_mid < k:
                left = mid
            else:
                right = mid - 1
        # left == right
        # answer = k - (arr[left] - (left + 1)) + arr[left]
        #          5 - (7 - (3 + 1)) + 7 = 5 - 3 + 7 = 9
        return k + left + 1