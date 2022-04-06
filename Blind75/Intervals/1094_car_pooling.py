"""
1094. Car pooling (Medium, 3 tagged 0 ~ 6 months)
https://leetcode.com/problems/car-pooling/

given capacity: int of a car, and trips: List[List[int]] of number of stop passengers,
 pick up and drop off location at each stop (relative to origin)
assuming the car only drives west to east, and all pick up and drop off locations are along the direction.

return true if it's possible to pickup and drop off all passengers for all the given trips, false otherwise
"""
from typing import List

# trip[i] = [numPassenger_i, from_i, to_i]
# at each from_i, we're picking up +numPassenger_i
# at each to_i, we're dropping off -numPassenger_i
# we can increment/decrement numPassenger at each event time/location, to update curr_numPassengers
# since there is chronological order, we need to increment/decrement from earliest to latest
# if at any given point, curr_numPassengers exceeds capacity, return false
# else, when loop finishes, return true


class Solution:
    def car_pooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_nPassengers = 0
        timestamp = []
        for n_passengers, pickup, dropoff in trips:
            timestamp.append((pickup, n_passengers))
            timestamp.append((dropoff, -n_passengers))
        timestamp.sort()
        for ts, passengers_change in timestamp:
            curr_nPassengers += passengers_change
            if curr_nPassengers > capacity:
                return False
        return True