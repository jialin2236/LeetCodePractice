"""
46. Permutations
Medium

Given an array nums of distinct integers,
return all the possible permutations. You can return the answer in any order.
"""

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
from typing import List


class Solution:
    def permutation(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def backtrack0(idx):
            if idx == n:
                ans.append(nums)
                return
            for i in range(idx, n):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack0(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
            return

        def backtrack1(arr, visited):
            if len(arr) == n:
                ans.append(arr)
                return
            for ni in nums:
                if ni not in visited:
                    arr.append(ni)
                    backtrack1(arr, visited.add(ni))
                    arr.pop()
                    visited.remove(ni)
            return

        backtrack0(0)
        return ans
                