"""
1762. Buildings With an Ocean View
https://leetcode.com/problems/buildings-with-an-ocean-view/

Medium
"""

# there are n buildings in a line. given an integer array heights of size n
# that represents the heights of the buildings in the line. 
# ocean is to the right of the building. a building has an ocean view 
# if the building can see the ocean without obstructions. Formally, a 
# building has an ocean view if all the buildings to its right have a smaller
# height. 

# return a list of indices of buildings that have an ocean view, sorted in
# increasing order

# example: [4,2,3,1] -> [0,2,3]
# loop through the array from the right hand end. 
# keep a max_height as we go, if heights[i] > max_height, 
# add i to ans, update max_height
max_height, ans = 0, []
for i in range(len(heights) - 1, -1, -1):
	if heights[i] > max_height: 
		ans.append(i)
		max_height = heights[i]
ans[::-1]