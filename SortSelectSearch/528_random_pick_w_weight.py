"""
528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight

Medium 
"""

# given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index
# implement pickIndex(), which randomly picks an index in the range [0, w.length - 1]
# the probability of picking an index i is w[i] / sum(w)

# example w = [1, 3], probability of picking index 0 is 1 / (1 + 3) = 0.25, probability
# of pikcing index 1 is 3 / (1 + 3) = 0.75. 

# Thoughts 
# Brute Force
# since each element some what represents a range, we can construct a new array listing
# every range element, arr = [(0, 1), (1, 1), (1, 2), (1, 3), ... ], uniformly select an index
# and return the value in arr. But space complexity would be very big
# we can sum(w) and randomly select a number from range(0, sum(w))
# we can view w as [(1), (1-3), (...)]
# traverse through w, and calculate the cumulative sum. As soon as cumulative sum > rand,
# the previous index is what we need. 

# [1, 2, 3] -> [0, 1, 2, 3, 4, 5]
import random
from typing import List

class Solution: 
	# if we want to sacrifice time complexity for space complexity 
	def __init__(self, w: List[int]):
		self.w = w
		self.total = sum(w)

	def pickIndex(self):
		idx = random.randint(0, self.total)
		i, cum_sum = 0, self.w[0]
		while i < len(self.w) - 1: 
			if cum_sum < idx: 
				i += 1
				cum_sum += self.w[i]
			else:
				break
		return i

class Solution_time: 
	# if we have extra space and would want to optimize time complexity
	def __init__(self, w: List[int]): 
		self.cumsum = []
		cs = 0
		for wt in w: 
			cs += wt
			self.cumsum.append(cs)
		self.total = cs

	def pickIndex(self): 
		target = random.randint(0, self.total)
		# binary search
		i, j = 0, len(self.cumsum)
		while i < j: 
			mid = i + (j - i) // 2
			if self.cumsum[mid] >= target and self.cumsum[mid - 1] < target: 
				return mid
			if self.cumsum[mid] < target: 
				i = mid + 1
			else: 
				j = mid - 1 
