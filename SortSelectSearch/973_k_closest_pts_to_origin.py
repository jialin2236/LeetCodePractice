"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin

Medium 
"""

# given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
# and an integer k, return the k closest points to the origin (0, 0)

# is k guarantee to be <= len(points)? 
# could points be empty array? 
# are points all integers? 

# idea
# we can use brute force approach to calculate each points distance to the origin
# rank them, and return the first k points
# time: O(NlogN)
# space: O(N)
distance = []
for x, y in points: 
	distance_i = math.sqrt(x ** 2 + y ** 2)
	distance.append([distance_i, x, y])
distance.sort(key=lambda x: x[0])
[[x, y] for d, x, y in distance[:k]]

# or use of a heap
# time: O(Nlogk)
# space: O(k)
def distance(x, y): 
	return x ** 2 + y ** 2 

for i in range(len(points)): 
	x, y = points[i]
	d = distance(x, y)
	points[i] = [d, x, y]
heapq.heapify(points)
ans = []
for i in range(k): 
	top = heapq.heappop(points)
	ans.append(top[1:])

# or we can try binary search
# first we need to determine the search space
# x_rng = [0, max_x], y_rng = [0, max_y]
points_abs = [abs(i) for x, y in points for i in [x, y]]

left, right = 0, max(points_abs)

def binary_search(candidates, left, right, k): 
	while left < right: 
		mid = left + (right - left) // 2
		in_bound = [[x, y] for x, y in candidates if abs(x) < mid and abs(y) < mid]
		if len(in_bound) == k:
			return in_bound
		elif len(in_bound) > k: 
			# too many points in bound of mid
			right = mid - 1
			candidates = in_bound
		else: 
			# not enough points in bound of mid
			left = mid + 1
			k -= len(in_bound)
			candidates = [pt for pt in points if pt not in in_bound]



# or we can use quick select, or heap select
def distance(point): 
	x, y = point
	return x ** 2 + y ** 2

def partition(points, left, right): 
	pvt_idx = random.randint(left, right)
	points[pvt_idx], points[right] = points[right], points[pvt_idx]
	pivot = distance(points[right])
	i = left
	for j in range(left, right): 
		if distance(points[j]) < pivot:
			points[i], points[j] = points[j], points[i]
			i += 1
	points[j], points[right] = points[right], points[j]
	return i

left, right = 0, len(points) - 1
def quick_select(points, left, right, k): 
	if left < right: 
		pi = partition(points, left, right, k)
		if pi - left == k - 1: 
			return points[left:pi]
		elif pi - left > k - 1: 
			# more than k elements before pi
			return quick_select(points, left, pi - 1, k)
		else: 
			# less than k elements before pi
			return quick_select(points, pi + 1, right, k - 1 + left - pi)




