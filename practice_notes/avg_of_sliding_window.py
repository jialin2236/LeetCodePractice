"""
I had initial phone screen with Meta for E5 position and here are the questions asked:

Find average of each Sliding window. Given an input array of n elements and a sliding window fo size k,
find the average of each sliding window.
input = [1,2,3,4,5]
k = 3
output = [2.0, 3.0, 4.0]
(1+2+3)/ 3 = 2.0
(2+3+4)/3 = 3.0
(3+4+5)/3 = 4.0

Expectation was to solve it in O(n) time and O(1) space
"""
from typing import List

class Solution:
    def sliding_window_avg(self, nums: List[int], k: int) -> List[float]:
        left, right = 0, k - 1
        total = 0
        ans = []
        while right < len(nums):
            if not ans:
                total += sum(nums[left:right+1])
            else:
                total += nums[right]
            ans.append(total/k)
            total -= nums[left]
            left += 1
            right += 1
        return ans