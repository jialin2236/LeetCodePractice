"""
31. Next Permutation (M, 94)
"""
from typing import List

# given nums: List[int]
# return the next permutation of the array
# 1234 -> 1243 -> 1324 -> 1342 -> 1423 -> 1432 -> 2134 -> 2314 -> 2413 -> 2431 ->
# 3124 -> 3214 -> 3412 -> 3421 -> 4123 -> 4213 -> 4231 -> 4312 -> 4321 -> 1234

# Observation
# at the end, nums should be sorted in desc order
# we need to start from the end of the array
# find the first occurence of nums[i-1] < nums[i]
# i - 1 would be your pivot point
class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        """
        time: O(n) - 2n
        space: O(1)
        :param nums:
        :return:
        """
        # change it in place
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        # nums[i-1] < nums[i]
        # we need to swap i - 1, with an element from nums[i:] that's barely larger than it
        # (minimum ele in nums[1:] that's bigger than nums[i-1])
        # since i - 1, i is the first incident from the end of nums that has nums[i-1] < nums[i]
        # all ele in nums[i:] is desc order, we can scan from end of array to find the first element larger
        # than nums[i-1], that's the min ele in nums[1:] that's bigger than nums[i-1], let's say its index is j

        j = n - 1
        if i > 0:
            while i > 0 and nums[j] < nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        # swap i - 1 and j
        # now we just need to reverse nums[i:] to get the next permutation
        # since j is the min ele in nums[i:] larger than nums[i-1], after swapping, nums[i:] is still ordered desc
        # like 2431 -> 3421, we now need to reverse nums[i:] to get 3124
        left, right = i, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

