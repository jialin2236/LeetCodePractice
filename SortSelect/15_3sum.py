"""
15. 3Sum 
https://leetcode.com/problems/3sum/

Medium 
"""

# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i!=j!=k and 
# nums[i] + nums[j] + nums[k] == 0

# example: nums = [-1,0,1,2,-1,-4]

# brute force is to try every 3 combination
# but the time complexity would be really high
# c_n_3, n factorial
# we can use a greedy approach
# nums.sort()
# start from the left of the array i
# i as the anchor index, let j = i + 1 and k = len(nums) - 1
# while j < k
# sum(nums[i,j,k]) > 0 -> we need a smaller number, move k to the left
# sum(nums[i,j,k]) < 0 -> we need a bigger number, move j to the right
# if sum(nums[i,j,k]) == 0, add nums[i,j,k] to answer, break loop
# increment i to the right. 
# since everything left of i has been explored, j = i+1 and k = len(nums) - 1
# repeat. 
# if nums[i+1] == nums[i], skip, since this combination has been explored.

def threeSum(nums):
	nums.sort()
	prev, ans = None, []
	for i in range(len(nums) - 3):
		if prev and nums[i] == prev:
			continue
		j = i + 1
		k = len(nums) - 1
		while j < k: 
			sub_arr = [nums[i], nums[j], nums[k]]
			total = sum(sub_arr)
			if total == 0: 
				ans.append(sub_arr)
				break
			if total < 0: 
				j += 1
			else: 
				k -= 1
		prev = nums[i]

# if asked a follow up question for no sort solution 
# use 2 hash tables, seen and dup
# seen to keep track of values previous loops have seen
# dup to skip duplicated element (to avoid duplicate elements in result)
def three_sum(nums):
	ans, dups = set(), set()
	seen = {}
	for i in range(len(nums)):
		if nums[i] not in dups:
			dups.add(nums[i])
			for j in range(i+1, len(nums)):
				complement = -nums[i] - nums[j]
				if complement in seen and seen[complement] == i:
					ans.add(tuple(sorted(nums[i], nums[j], complement)))
				seen[nums[j]] = i
	return ans



