"""
339. Nested List Weight Sum (M, 107)
"""

# what we know
# given a nested list
# depth of an int: number of lists that it is inside of
# return the sum of each integer in list, multiply by its depth

# can we do a dfs?
# input: List[NestedInteger]
# NestedInteger Operations: isInteger, getInteger, getList
from NestedList import NestedInteger
from typing import List
from collections import deque

# perform a dfs on a NestedInteger, with depth as an input
# dfs(nested_int, depth):
#    if nested_int isInteger -> total += depth * getInteger
#    else -> is a list -> nested_list = getList
#                         -> for ele in nested_list, dfs(ele, depth + 1)
# recursively compute total

class Solution:
    def depth_sum(self, nestedList: List[NestedInteger]) -> int:
        """
        time: O(n)
        space: O(h)
        :param nestedList:
        :return:
        """
        total = 0

        def dfs(nested: NestedInteger, depth: int) -> None:
            if nested.isInteger():
                nonlocal total
                total += nested.getInteger() * depth
            else:
                for ele in nested.getList():
                    dfs(ele, depth + 1)

        for nested_ele in nestedList:
            dfs(nested_ele, 1)
        return total

    def depth_sum_bfs(self, nestedList: List[NestedInteger]) -> int:
        """
        time: O(n)
        space: O(n)
        :param nestedList:
        :return:
        """
        total, depth = 0, 1
        queue = deque(nestedList)
        while queue:
            for i in range(len(queue)):
                nested = queue.popleft()
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    queue.extend(nested.getList())
            depth += 1
        return total