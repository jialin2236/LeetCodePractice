"""
480. Sliding Window Median
Hard

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very
left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
"""
from typing import List, Tuple
import heapq
import bisect

class Solution:
    def find_median(self, nums: List[int], start: int, n: int) -> List[float]:
        lis = []
        for idx in range(n):
            lis.append(nums[start + idx])
        lis.sort()
        mid = (n - 1) // 2
        if n % 2 == 0:
            # even number
            return [lis[start + mid], lis[start + mid + 1]]
        else:
            return [lis[start + mid]] * 2

    def sliding_win_med(self, nums: List[int], k: int) -> List[float]:
        mi = self.find_median(nums, 0, k)
        ans = [sum(mi)/2]
        i, j = 1, k
        while j < len(nums):
            if nums[i-1] == mi[0]:
                if nums[i-1] <= nums[j] <= mi[1]:
                    mi[0] = nums[j]
                else:
                    mi = self.find_median(nums, i, k)
            elif nums[i-1] == mi[1]:
                if mi[0] <= nums[j] <= nums[i-1]:
                    mi[1] = nums[j]
                else:
                    mi = self.find_median(nums, i, k)
            elif (nums[i-1] < mi[0] and nums[j] > mi[1]) or (nums[i-1] > mi[1] and nums[j] < mi[0]):
                mi = self.find_median(nums, i, k)
            ans.append(sum(mi)/2)
            i += 1
            j += 1
        return ans

    def medianSlidingWindow(self, nums, k):
        small, large = [], []
        for i, x in enumerate(nums[:k]):
            heapq.heappush(small, (-x, i))
        for _ in range(k - (k >> 1)):
            # (k - k//2)
            move(small, large)
        ans = [get_med(small, large, k)]
        for i, x in enumerate(nums[k:]):
            if x >= large[0][0]:
                heapq.heappush(large, (x, i+k))
                if nums[i] <= large[0][0]:
                    # remove element i out of the window scope
                    # balance the 2 heap sizes (since we're removing num[i] from small)
                    move(large, small)
            else:
                heapq.heappush(small, (-x, i+k))
                if nums[i] >= large[0][0]:
                    move(small, large)
            while small and small[0][1] <= i:
                heapq.heappop(small)
            while large and large[0][1] <= i:
                heapq.heappop(large)
            ans.append(get_med(small, large, k))
        return ans

def move(h1, h2):
    x, i = heapq.heappop(h1)
    heapq.heappush(h2, (-x, i))

def get_med(h1, h2, k):
    return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.


def medianSlidingWindow(self, nums, k):
    medians, window = [], []
    for i in range(len(nums)):
        # Find position where outgoing element should be removed from
        if i >= k:
            # window.remove(nums[i-k])        # this works too
            # bisect.bisect(a, x, lo=0, hi=len(a))
            # returns an insertion point which comes after (to the right of) any existing entries of x in a.
            window.pop(bisect.bisect(window, nums[i - k]) - 1)
        # Maintain the sorted invariant while inserting incoming element
        bisect.insort(window, nums[i])
        # Find the medians
        if i >= k - 1:
            medians.append(float((window[k / 2]
                                  if k & 1 > 0
                                  else(window[k / 2 - 1] + window[k / 2]) * 0.5)))
    return medians