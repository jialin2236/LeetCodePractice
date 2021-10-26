# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        comp_lookup = {}
        for i in range(len(nums)):
            comp_i = target - nums[i]
            if comp_i in comp_lookup.keys():
                return [i, comp_lookup[comp_i]]
            else:
                comp_lookup[nums[i]] = i


s = Solution()
t1 = s.twoSum([3,2,4],6)
print(t1)