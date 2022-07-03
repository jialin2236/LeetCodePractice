"""
708. Insert into a Sorted Circular Linked List (M, 33)
"""

from typing import Optional

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# given head: Optional[Node], insertVal: int
# insert insertVal into proper position in circular linked list (sorted asc)
# if input linked list is empty, create a new list and return the reference to that single node

class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> Node:
        """
        time: O(N)
        space: O(1)
        :param head:
        :param insertVal:
        :return:
        """
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node
        prev = head
        curr = head.next
        while curr != head:
            # 1. prev <= curr
            if prev.val <= curr.val:
                if prev.val < insertVal <= curr.val:
                    # prev and curr are of right order and insertVal falls between them
                    break
            # 2. # prev.val > curr.val, we reached the max -> min transition
            elif insertVal > prev.val or insertVal <= curr.val:
                break
            prev, curr = curr, curr.next
        prev.next, new_node.next = new_node, curr
        return head