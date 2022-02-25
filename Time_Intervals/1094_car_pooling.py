"""
1094. Car Pooling
https://leetcode.com/problems/car-pooling/

Medium
"""

# input: 
# capacity - car with capacity empty seats
# trips - array where trips[i] = [numPassengers_i, from_i, to_i]
# from, to - are distance from the car's initial location
# example: 
# trips: [[2, 1, 5], [3, 3, 7]], capacity = 4
# question: is the input sorted by the origin location? 
# is numPassengers in each trip guarenteed to be <= capacity? 
# thoughts: 
# by using a timestamp to record nPassenger change spots
class Solution:
	def enough_room(self, trips, capacity):
		timestamp = []
		for trip in trips:
			timestamp.append([trip[1], trip[0]])
			timestamp.append([trip[2], -trip[0]])

		timestamp.sort()
		curr_passengers = 0
		for t in timestamp:
			curr_passengers += t[1]
			if curr_passengers > capacity:
				return False
		return True

	def enough_room_ii(self, trips, capacity):
		pickup = min([p for n, p, d in trips])
		dropoff = max([d for n, p, d in trips])

		passengers = [0] * (dropoff - pickup + 1)

		for n, i, j in trips:
			passengers[i] += n
			passengers[j] -= n

		for i in passengers:
			capacity -= i
			if capacity < 0:
				return False
		return True



# finding the max overlap point
def maxOverlap(intervals): 
	interval_pts = []
	for interval in intervals: 
		left, right = interval
		interval_pts.append([left, 1])
		interval_pts.append([right, -1])
	interval_pts.sort()
	max_pts, curr_pts = 0, 0
	max_index = 0 
	for pt in interval_pts:
		curr_pts += pt[1]
		if curr_pts > max_pts: 
			max_pts = curr_pts
			max_index = pt[0]









