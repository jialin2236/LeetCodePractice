"""
346. Moving Average from Data Stream (E, 39)
"""
from collections import deque
# implement a class MovingAverage
# class properties: size, as size of the moving average window
# function next(val: int) -> float, to calculate the moving average of the last size values of the stream

# use the property of a queue: FIFO

class MovingAverage:
    """
    time: O(1)
    space: O(N) N being the window size
    """
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        while len(self.queue) >= self.size:
            self.total -= self.queue.popleft()
        # now len(queue) < size
        self.total += val
        self.queue.append(val)
        return self.total / len(self.queue)