"""
346. Moving Average from Data Stream (Easy, 34 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/moving-average-from-data-stream/

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:

MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.
"""
from collections import deque
# example
# input: ["MovingAverage", 3], ["next, 1], ["next", 10], ["next", 3], ["next", 5]
# output: [None, 1, 5.5, 4.667, 6]

class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque(maxlen=size)

    def next(self, val: int) -> float:
        q = self.queue
        q.append(val)
        return float(sum(q))/len(q)
