"""
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/

Medium 
"""

# Questions: 
# 1. Do the 3 integers need to be consecutive in the input array? 
# 2. Are all numbers in input array integers? 
# 3. by closest, can it be smaller or larger? 

# Thoughts: 
# 1. we can sort the array
# 2. loop through the array
# 3. in each iteration, set left pointer as idx + 1, and right pointer as n - 1
# 4. sum values at idx, left, right. calculate gap with target, assign to diff
# 	- gap < 0 -> we need higher value -> increment left
# 	- else -> we need lower value -> decrement right
# 5. update diff if new gap is closer than current diff
# 6. break if diff == 0
# 7. if value at idx is identical to value at idx - 1, skip 

def sum3_closest(nums, target): 
	diff = -math.inf
	nums.sort()
	for i in range(len(nums)): 
		j, k = i + 1, len(nums) - 1
		while j < k: 
			res = nums[i] + nums[j] + num[k]
			if abs(target - res) < abs(diff): 
				diff = target - res
			if res < target: 
				j += 1
			else:
				k -= 1
		if diff == 0: 
			break
	return target - diff 
