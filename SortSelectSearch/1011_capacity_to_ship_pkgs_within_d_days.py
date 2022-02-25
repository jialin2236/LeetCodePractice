"""
1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
similar: 
https://leetcode.com/problems/split-array-largest-sum/

Medium
"""

# question:
# 1. are wieghts sorted? 
# thoughts: 
# 1. build a helper function with a proposed capacity as input, and return whether 
# 	 or not it is feasible to ship all weights within `days` given proposed capacity
# 2. min_capacity = avg(weights), max_capacity = sum(weights)
# 3. binary search between min and max capacity, return min feasible capacity

def ship_within_days(weights, days): 
	def feasible(capacity): 
		total, n_days = 0, 1
		for i in range(len(weights)): 
			total += weights[i]
			if total > capacity:
				total = weights[i]
				n_days += 1
				if n_days > days: 
					return False
		return True

	left, right = sum(weights)/days, sum(weights)
	while left < right: 
		mid = left + (right - left)//2
		mid_feasible = ship_within_days(mid)
		if mid_feasible: 
			right = mid
		else: 
			left = mid + 1
	return left 