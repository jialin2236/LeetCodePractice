"""
658. Find K Closest Elements (Medium)
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array.
The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
"""
from typing import List

# since the array is sorted already, we can use binary search to look for the
# left boundary of the answer, and return arr[left_bound:left_bound + k]

# to find the left boundary of the answer, we can use a modified binary search
# given array length as n, left boundary is [0,...,n - k]
# to conduct binary search within the space of [0, n - k]
# compare arr[mid] with arr[mid + k]
# if arr[mid] is closer to x compared to arr[mid + k]
# -> arr[mid:mid + k - 1] is a closer option than arr[mid + 1:mid + k], move search space to left -> right = mid
# if arr[mid + k] is closer to x
# -> arr[mid + 1:mid + k] is a closer option than arr[mid:mid + k - 1], move search space to right -> left = mid + 1
# until binary search converge

def find_closest_ele(arr: List[int], k: int, x: int) -> List[int]:
    """
    time: O(log(N-K)) - for binary search
    space: O(1)
    :param arr:
    :param k:
    :param x:
    :return:
    """
    n = len(arr)
    left, right = 0, n - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            # ...arr[mid]......x...arr[mid + k]...
            # ...arr[mid]......arr[mid + k]...x...
            left = mid + 1
        else:
            # ...x...arr[mid]......arr[mid + k]
            # ...arr[mid]...x......arr[mid + k]
            right = mid
    return arr[left:left + k]