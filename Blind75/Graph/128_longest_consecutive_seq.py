"""
128. Longest Consecutive Sequence (Medium, 4 fb tagged 0-6 months)
https://leetcode.com/problems/longest-consecutive-sequence/

given an unsorted array nums: List[int]

return the length of the longest consecutive elements sequence in O(n) time
"""
from typing import List
from collections import defaultdict

# use a hash/set

class Solution:
    def longest_seq(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in nums_set:
                curr = num
                streak = 1
                while curr + 1 in nums:
                    curr += 1
                    streak += 1
                ans = max(ans, streak)
        return ans

    def longeest_seq_hash(self, nums: List[int]) -> int:
        seq_dict = {i: [] for i in nums}
        for ele in nums:
            if (ele - 1) in seq_dict:
                seq_dict[ele - 1].append(ele)
            if (ele + 1) in seq_dict:
                seq_dict[ele + 1].append(ele)

        seen, ans = set(), 0

        def dfs(i, size):
            seen.add(i)
            size += 1
            for j in seq_dict[i]:
                if j not in seen:
                    dfs(j, size)

        for ele in nums:
            if ele not in seen:
                seq_size = 0
                dfs(ele, seq_size)
                ans = max(ans, seq_size)

        return ans