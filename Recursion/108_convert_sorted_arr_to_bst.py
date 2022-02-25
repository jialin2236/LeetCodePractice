from typing import List, Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def arrToBST(self, arr: List[int]) -> Optional[Node]:
        def helper(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            root = Node(arr[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(arr) - 1)
