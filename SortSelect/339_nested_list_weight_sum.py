"""
339. Nested List Weight Sum
Medium

You are given a nested list of integers nestedList.
Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example,
the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.
"""
from typing import List

class NestedInteger:
    def __init__(self, value=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

    def add(self, elem):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
        """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class Solution:
    def nested_sum(self, nestedList: List[NestedInteger]) -> int:
        def nested_sum_util(sub_nested:List[NestedInteger], depth: int) -> int:
            total = 0
            for e in sub_nested:
                if e.isInteger():
                    total += e.getInteger() * depth
                else:
                    total += nested_sum_util(e.getList(), depth + 1)
            return total
        return nested_sum_util(nestedList, 1)
