"""
1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
similar: 
https://leetcode.com/problems/split-array-largest-sum/

Medium
"""
from typing import List

# question:
# 1. are wieghts sorted? 
# thoughts: 
# 1. build a helper function with a proposed capacity as input, and return whether 
# 	 or not it is feasible to ship all weights within `days` given proposed capacity
# 2. min_capacity = max(weights) just to ensure the largest package would fit into the ship
# 	 max_capacity = sum(weights) if everything is to be shipped out on one single day
# 3. binary search between min and max capacity, return min feasible capacity

class Solution:
	def shipWithinDays(self, weights: List[int], days: int) -> int:
		def valid_capacity(capacity):
			curr_cap = capacity
			n_days = 1
			for wt in weights:
				curr_cap -= wt
				if curr_cap < 0:
					curr_cap = capacity - wt
					n_days += 1
					if n_days > days: return False
			return True

		lb, ub = max(weights), sum(weights)
		while lb < ub:
			mid = (lb + ub) // 2
			if valid_capacity(mid):
				ub = mid
			else:
				lb = mid + 1
		return lb