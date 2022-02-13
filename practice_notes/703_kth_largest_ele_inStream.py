"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element
in the stream.
"""
from typing import List, Optional
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.kth = self.kth_largest(nums, k)

    def kth_largest(self, arr: List[int], k: int) -> Optional[int]:
        def heapify(arr: List[int], i: int, j: int) -> None:
            lc = 2*i + 1
            rc = 2*i + 2
            parent = i
            if lc < j and arr[lc] > arr[parent]:
                parent = lc
            if rc < j and arr[rc] > arr[parent]:
                parent = rc
            if parent != i:
                arr[parent], arr[i] = arr[i], arr[parent]
                heapify(arr, parent, j)

        if k > len(arr) or not k:
            return None
        n, p = len(arr) - 1, len(arr)//2 - 1
        while p > 0:
            heapify(arr, p, n)
            p -= 1
        for cnt in range(1,k):
            arr[0], arr[-1] = arr[-1], arr[0]
            tmp = arr.pop()
            heapify(arr, 0, n - cnt)
        return tmp

    def add(self, val: int) -> int:
        self.nums.append(val)
        if val > self.kth:
            self.kth = self.kth_largest(self.nums, self.k)
        return self.kth


class Kth_Largest: 
    def __init__(self, nums: List[int], k: int): 
        self.k = k
        self.heap = heapq.heapify(nums)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int: 
        heapq.heappush(val, self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        return self.heap[0]




        