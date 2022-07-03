"""
88. Merge Sorted Arrays (E)
"""
from typing import List
# input nums1: List[int], nums2: List[int], m: int, n: int
# m as size of nums1, n as size of nums2
# merge the 2 sorted array to a sorted array in-place to nums1
# nums1 is of size m + n with the last n elements being zeros

# start from the end
class Solution:
    def merge_arr(self, nums1: List[int], nums2: List[int], m: int, n: int) -> None:
        # pointers for iterating in nums1, nums2 and the combined array
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 or j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if j >= 0: 
            nums1[:k+1] = nums1[:j+1]