"""
825. Friends of Appropriate Ages (M)
"""
from typing import List

# n persons on a social media website
# input ages: List[int], ages[i] is the age of ith person
# x will not send a friend request to y if any of the following conditions is true
#   ages[y] <= 0.5*ages[x] + 7
#   ages[y] > ages[x]
#   ages[y] > 100 and ages[x] < 100
# -> 2 and 3 are redundant
# -> x will send request to y if
#       ages[y] > 0.5*ages[x] + 7 AND ages[y] <= ages[x]


# since there are only 120 possible ages
# we can construct a fix length array to store the number of people at each age
# when we loop through the age count array, by calculating the AND condition above
# ages[y] > 0.5*ages[x] + 7 AND ages[y] <= ages[x], we can get the lower bound and upper bound of friend
# by summing up the subarray of [lower_bound, upper_bound], we get the total of request sent by people in age_count[i]
# decrement that number by sum - age_count[i] (can't request to person themselves)

class Solution:
    def num_frd_req(self, ages: List[int]) -> int:
        age_cnt = [0 for _ in range(121)]
        for a in ages:
            age_cnt[a] += 1

        total = 0
        for age, cnt in enumerate(age_cnt):
            frd_lb = int(0.5 * age) + 8
            frd_ub = age
            if frd_lb <= frd_ub:
                reqs = sum(age_cnt[frd_lb:frd_ub + 1]) * cnt
                reqs -= cnt
                total += reqs
        return total