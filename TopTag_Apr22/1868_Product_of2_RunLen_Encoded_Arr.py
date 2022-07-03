"""
1868. Product of Two Run-Length Encoded Arrays (Medium, 16 tagged)
https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

Run-length encoding: compression algo that represents consecutive repeated numbers in an integer array by a 2D array
                     encoded. encoded[i] = [val_i, freq_i] describes the ith segment of repeated numbers in nums
Example: nums = [1,1,1,2,2,2,2,2,] -> encoded = [[1,3],[2,5]] (3 1's followed by 5 2's)

The product of two run-length encoded arrays encoded1, encoded2 can be calculated as
1. expand both encoded1 and encoded2 into full arrays nums1 and nums2
2. create a new array prodNums of length len(nums1), prodNums[i] = nums1[i] * nums2[i]
3. compress prodNums into a run-length encoded array and return it

given encoded1, encoded2 representing nums1 and nums2, len(nums1) = len(nums2)
"""
from typing import List

# Approach
# nums1 = [v for val, freq in encoded1 for v in [val] * freq]
# nums2 = [v for val, freq in encoded2 for v in [val] * freq]
# prodNums = []
# for i in range(len(nums1)): prodNums.append(nums1[i] * nums2[i])
# prev = freq = None
# for ele in prodNums:
#     if not prev or ele != prev:
#        if freq: ans.append([prev, freq])
#        prev = ele
#        freq = 1
#     else:
#        freq += 1
# ans.append([prev, freq])

class Solution:
    def find_rle_arr(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        :param encoded1:
        :param encoded2:
        :return:
        """
        i = j = frq1 = frq2 = v1 = v2 = 0
        m, n, ans = len(encoded1), len(encoded2), []
        while i < m or j < n:
            if not frq1 and i < m:
                v1, frq1 = encoded1[i]
            if not frq2 and j < n:
                v2, frq2 = encoded2[i]
            min_freq, product = min(frq1, frq2), v1 * v2
            if ans and ans[-1][0] == product:
                ans[-1][0] += min_freq
            else:
                ans.append([product, min_freq])
            frq1 -= min_freq
            frq2 -= min_freq
            i += 1 if not frq1 else 0
            j += 1 if not frq2 else 0
        return ans

    def find_rle_arr0(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = idx = 0
        ci = cj = 0
        prev = None
        cnt = 0
        while i < len(encoded1) and j < len(encoded2):
            p = encoded1[i][0] * encoded2[j][0]
            if not prev or p != prev:
                if prev:
                    ans.append([prev, cnt])
                prev = p
                cnt = 0
            cnt += 1
            idx += 1
            if encoded1[i][1] + ci == idx + 1:
                ci += encoded1[i][1]
                i += 1
            if encoded2[j][1] + cj == idx + 1:
                cj += encoded2[j][1]
                j += 1
        return ans