"""
1762. Buildings With an Ocean View (M, 157)
"""
from typing import List

# what we know
# input - heights: List[int]
# ocean to the right of buildings -> ocean after the end of the array?
# return list of indices of buildings with an ocean view, sorted in increasing order (index)
# since ocean is on the right, and without knowing traversing the whole list, we don't know the height of each
# building -> iterate array from the right, time: cannot do better than O(N)
# for each building, if any building on the right is higher -> no view. we keep a max_height variable and update it

def find_buildings(height: List[int]) -> List[int]:
    """
    time: O(N)
    space: O(1)
    :param height:
    :return:
    """
    max_height = 0
    ans = []
    for i in range(len(height) - 1, -1, -1):
        if height[i] > max_height:
            ans.append(i)
            max_height = height[i]
    # ans now has all the indices that is the tallest so far, when iterating array from the end
    # since we start appending indices from the end, and problem asks us to return it sorted in increasing order
    return ans[::-1]