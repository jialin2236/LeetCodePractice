"""
636. Exclusive Time of Functions (M, 29)
"""
from typing import List
# we have a single thread CPU, and n functions
# given logs: List[str], logs[i] = "id:event:timestamp"
# "start": beginning of the timestamp minute, "end": end of the timestamp minute
# return exclusive time of each function in an array

class Solution:
    def exclusive_time(self, logs: List[str], n: int) -> List[int]:
        res = [0 for _ in range(n)]
        stack = []
        for event in logs:
            i, action, ts = event.split(":")
            if action == 'start':
                stack.append((int(i), int(ts)))
            else:
                # action is ending function that's on top of the stack
                prev_i, prev_ts = stack.pop()
                interval = ts - prev_ts + 1
                res[prev_i] += interval
                # if stack is not empty, top of stack function was not running during interval
                # but would be accounted for in later step due to ts - prev_ts + 1 step
                # decrement the interval to top of stack function ahead of time
                if stack:
                    res[stack[-1][0]] -= interval
        return res