"""
1570. Dot Product of Two Sparse Vectors (M, 135)
"""
from typing import List

# what we know
# 2 sparse vectors, compute dot product
# implement a class to do so
# condense each sparse vector into a vector indicating index and value
# compute the dot product based on that

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_vec = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.nums_vec[i] = nums[i]

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, v in self.nums_vec.items():
            if i in vec.nums_vec:
                res += v * vec.nums_vec[i]
        return res

    # follow up, if the 2 vectors have different level of sparseness
    # how to optimize
    #     res = 0
    #     v1, v2 = (self.nums_vec, vec.nums_vec) if len(self.nums_vec) <= vec.nums_vec else (vec.nums_vec, self.nums_vec)
    #     for i, v in v1.items():
    #         if i in v2:
    #             res += v * v2[i]
    #     return res
