# 5 longest palindromic substring
# Given a string s, return the longest palindromic substring in s. 

# criteria
# needs to be a substring of s (does it include s?)
# needs to be a palindromic string itself
# does a single character string count as palindromic, what about emtpy? 
# could the input be null? what if there is a tie? 

# we need to traverse the string
# keep track of the max_len of palindromic substring
# can we use a sliding window? 
# 'abccbaakij', 'abcbaakij' -> non-trivial palindromic string is of odd or even
# length. Odd length, s[mid-i] == s[mid+1], even length, s[mid] == s[mid+1]
# have a helper function to expand count from a middle index, 
# and stop when it's no longer plaindromic
# for a given non null string, length is at least 1

def longest_palindrome(s: str) -> str: 
	def helper(start, end): 
		# expand window using the 2 pointers
		# till substring is no longer palindromic
		# return the size of the palindromic string
		while start and end < n and s[start - 1] == s[end + 1]: 
			start -= 1
			end += 1
		return start - end + 1

	i, n = 1, len(s)
	max_len, start_idx = 0, ''
	while i < n:
		if i > n - max_len: 
			break 
		# 1. s[i - 1] == s[i] == s[i + 1] -> start exploring s[i - 2], s[i + 2]
		# 2. s[i] == s[i + 1] -> s[i - 1], s[i + 2]
		# 3. s[i], s[i]
		if s[i] == s[i + 1]: 
			window = helper(i - 1, i + 1) if s[i - 1] == s[i] else helper(i, i + 1)
		else: 
			window = helper(i, i)
		if window > max_len: 
			max_len = window
			start_idx = i - window//2
		i += 1
	return s[start_idx:start_idx + max_len]


# 11. container with most water
# integer array `height` of size n. Find 2 lines that the container holds 
# most water, return max amount of water it holds

# do the middle lines have any effect on how much water the container holds? 
# ex: [5,1,2,6], if we choose 5 and 6, does it mean it holds 5 * (3 - 0) unit?

# we can use 2 pointers and start from the 2 ends of the array. (i, j)
# since the lower of the 2 heights determine the height of the container
# we want to improve on that end. units = min(height[i], height[j]) * (j - i)
# squeeze the end that's shorter. re-calculate units, update if increases. 
# until the 2 pointers meet. 

def most_water(height): 
	i, j = 0, len(height) - 1
	ans = 0
	while i < j: 
		units = min(height[i], height[j]) * (j - i)
		ans = max(ans, units)
		if s[i] < s[j]: 
			i += 1
		else: 
			j -= 1
	return ans 


# 22. generate parentheses
# given n paris of parentheses, generate all combinationrs of well formed parentheses

# ')'? 
# return a list of strings? 
# it asks us to enumerate all possible combination that feasible, we can use backtracking
# as a general idea with defining what the feasibility criteria is

# knowing n, we know the length of any qualifying string is 2 * n, since each 
# pair there's '(' and ')'
# so once the control pointer reaches 2 * n, we can append the string to output
# otherwise, for s in ['(', ')'], if string += s is valid, add in and backtrack, pop

def parentheses(n):
	ans = []
	def backtrack(string, n_open, n_close): 
		if len(string) == 2*n: 
			ans.append(string)
			return
		if n_open < n: 
			string += '('
			backtrack(string, n_open + 1, n_close)
			string -= '('
		if n_close < n_open: 
			string += ')'
			backtrack(string, n_open, n_close + 1)
			string -= ')'
	backtrack('', 0, 0)
	return ans


# 34. find first and last position of element in sorted array
# given an array of integers nums, sorted in non-decreasing order. And an integer
# target. Find the starting and ending positiong of given target value. 

# search in a sorted array
# the brute force method would be to use linear search, and return first and
# last occurence, break loop when last target value is found
# this would take O(n) time
def find_range_linear(nums, target): 
	# linear scan
	left, right = -1, -1
	for i in range(len(nums)): 
		if nums[i] == target: 
			if left == -1:
				left = i
			else: 
				right = i
		else: 
			if left > -1 and right > -1: 
				break
	return [left, right]

# we can also use binary search since the array is already sorted
# find the left edge first, then use the left edge as lower bound, find the right edge
# nums[mid] == target, if mid == left or nums[mid-1] < target -> left boundary
# else, right = mid - 1
# similarly, find right boundary 


def find_range(nums, target): 
	def find_bound(left, right, lower): 
		while left < right: 
			mid = left + (right - left) // 2
			if nums[mid] < target: 
				left = mid + 1
			elif nums[mid] > target: 
				right = mid - 1
			else: 
				if lower: 
					if mid == left or nums[mid - 1] < target: 
						return mid
					right = mid - 1
				else: 
					if mid == right or numd[mid + 1] > target: 
						return mid
					left = mid + 1
		return -1

	n = len(nums)
	lower = find_bound(0, n - 1, True)
	if lower == -1: 
		return [-1, -1]
	upper = find_bound(0, n - 1, False)
	return [lower, upper]

# 46. Permutations 
# given an array nums of distinct integers, return all possible permutation 

def permutation(nums): 
	n, ans = len(nums), []
	seen = set()
	def backtrack(idx, combo, remain): 
		if idx == n: 
			ans.append(combo)
			return 
		for j in range(n):
			if nums[j] not in seen: 
				seen.add(nums[j])
				combo.append(s[j])
				backtrack(idx + 1, combo, cnt)
				combo.pop()
				seen.remove(nums[j])

# 24. swap nodes in pairs 
# given a linked list, swap every 2 adjacent nodes and return its head. Solve the problem 
# without modifying the values in the list nodes
# what if the input list has odd number of nodes? 

class ListNode: 
	def __init__(self, val): 
		self.val = val 
		self.next = None

def swap_nodes_recursive(head): 
	if not head or not head.next: 
		return head
	swap = head.next
	remain = swap.next
	swap.next = head
	head.next = swap_nodes(remain)
	return swap


def swap_nodes_iterative(head): 
	if not head or not head.next: 
		return head
	prev = ListNode(0)
	prev_initial = prev 
	prev.next = head
	while head and head.next: 
		swap = head.next
		remain = swap.next
		prev.next = swap
		swap.next = head
		head.next = remain
		prev = head
		head = remain
	return prev_initial.next


# 48. Rotate Image
# you're given an n * n 2D matrix representing an image, rotate the image by 90 degrees. 
# modify in place
# example:   [[1,2,3],   [[7,4,1],
			# [4,5,6], 	  [8,5,2],
			# [7,8,9]] -> [9,6,3]]
# rotate clockwise 90 degrees: 
# [i,j] -> [n - j - 1, i]
# transpose the matrix first 
# [[1,4,7], 
#  [2,5,8],
#  [3,6,9]] 
# for each row, rotate
# [[7,4,1],
#  [8,5,2],
#  [9,6,3]] done
def rotate_image(matrix):
	for i, j in range(n): 
		# transpose the entire matrix
		matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	for i in range(n):
		left, right = 0, n-1
		while left < right: 
			matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
	return matrix

# 49. group anagrams
# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# example: ['eat','tea','tan','ate','nat','bat']
# how to identify anagrams 
# 1. sort each string, use it as a key in a lookup table could be O(nlogn)
# 2. create a count array as key 

def group_anagrams(strs):
	lookup = collections.defaultdict(list)
	for s in strs: 
		s_sort = sorted(s)
		lookup[s_sort].append(s)
	return [i for i in lookup.items()]


# 75. sort colors
# given an array nums with n objects colored red, white, or blue. 
# sort them in-place so that objects of the same color are adjacent
# with the colors in the order red, white, and blue (0,1,2)
# cannot use the library's sort function. 

# example: 
# nums = [2,0,2,1,1,0] -> [0,0,1,1,2,2]
# use quick sort to sort this in place, or heap sort
# or we can use 3 pointers and swap as needed 
# ideally we want to place 0 at the left and 2 at the right, 1 in the middle
# question: is it guarantee to have 0,1 and 2 in the array, with none missing? 
# if we use curr as a pointer to control which index we're examining
# use left as a pointer to indicate left most index we need to swap for
# right to indicate right most index we need to swap for
# squeeze left/right pointer after swapping, move curr index + 1

def sort_colors(nums): 
	curr, left, right = 0, 0, len(nums) - 1
	while curr < right:
		if curr == 0:
		# current index is of 0, we need to swap it with left pointer (needs zero) 
			nums[curr], nums[left] = nums[left], nums[curr]
			left += 1
			curr += 1
		if curr == 2: 
			nums[curr], nums[right] = nums[right], nums[curr]
			right -= 1
		else: 
			curr += 1

# binary tree in order traversal
# both recursive and iterative methods takes O(n) time and space complexity
# in order to achieve O(1) space complexity (O(2n) -> O(n) time), we utilizes the 
# Morris traversal 


def morris_inorder(root):
	nodes = []
	curr = root
	while curr: 
		if curr.left: 
			prev = curr.left 
			while prev.right and prev.right != curr:
				prev = prev.right
			if not prev.right: 
				prev.right = curr
				curr = curr.left 
			else: 
				prev.right = None 
				nodes.append(curr.val)
				curr = curr.right
		else: 
			nodes.append(curr.val)
			curr = curr.right

# 454. 4Sum II 
# Given four integer arrays nums1, nums2, nums3, nums4 
# all of length n, return number of tuples (i, j, k, l)
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0













