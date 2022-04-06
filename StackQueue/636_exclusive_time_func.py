"""
636. Exclusive Time of Functions (Medium)
https://leetcode.com/problems/exclusive-time-of-functions/

Environment: Single threaded CPU

Input:
n (number of functions)
logs (List of "function_id:action:timestamp" like "1:start:0")

Output:
list of exclusive time of each function in an array (exclusive time: total runtime of a function)

Note: Single threaded CPU means it can only run one function at a time, functions that are already started will be
      picked up again when current function is finished running. And the waiting time is not considered into the
      exclusive time.
"""
import collections
from typing import List


class Solution:
    def exclusive_time(self, n: int, logs: List[str]) -> List[int]:
        logs_arr = [[int(i), a, int(ts)] for log in logs for (i, a, ts) in [log.split(':')]]
        logs_arr.sort(key=lambda x: x[2])
        start = collections.deque()
        res = [0] * n
        for i, action, ts in logs_arr:
            if action == "start":
                start.append((i, ts))
            else:
                prev_i, prev_ts = start.pop()
                duration = ts - prev_ts + 1
                res[prev_i] += duration
                if start:
                    next_i, next_ts = start[-1]
                    res[next_i] -= duration
        return res