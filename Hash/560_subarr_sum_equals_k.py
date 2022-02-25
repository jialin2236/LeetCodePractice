"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Medium
"""

"""
given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k

nums: [n0, n1, n2, ...]
k: k

is it guarantee to be a solution? could there be 0 of them? 
could the input be empty? could k be <= 0? 
are all elements in nums positive? 

we can use a sliding window? 
ans = 0
i, j = 0, 0
while j < len(num): 
	if current window sum < k: expand window to the right
	if current window sum > k: squeeze window from the left
	if current window sum == k: increment ans, expand window to the right

SLIDING WINDOW WILL NOT WORK as some elements are allowed to be negative 
"""

"""
hashmap? 
loop through the array
cum_sum = Counter()
cum_sum[0] = 1
res = k - cum_sum[i]
if res exist in cum_sum: ans += 1
"""

from typing import List

def subarray_sum(nums: List[int], k: int) -> int: 
	cumulative = collections.Counter()
	cumulative[0] += 1
	ans, curr = 0, 0
	for num in nums:
		curr += num
		res = k - curr
		if res in cumulative: 
			ans += cumulative[res]
		cumulative[curr] += 1
	return ans