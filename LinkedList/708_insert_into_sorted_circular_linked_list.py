"""
708. Insert into a Sorted Circular Linked List (Medium, 27 fb tagged 0 ~ 6 mths)
https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

Given a Circular Linked List node, which is sorted in ascending order,
write a function to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null),
you should create a new single circular list and return the reference to that single node.
Otherwise, you should return the originally given node.
"""
from typing import Optional
from LinkedList import LinkedNode

# example
# head = 3
# 1 -> 3
# |    |
#  <-  4    to 1 -> 2 -> 3 -> 4 -> 1 ...

# 2 scenarios to insert the value
# 1. insertVal between node and node.next
# 2. when reaching the beginning/end of the circular list, insertVal > node or insertVal < node.next

class Solution:
    def insert(self, head: Optional[LinkedNode], insertVal: int) -> LinkedNode:
        node = LinkedNode(insertVal)
        if not head:
            node.next = node
            return node
        prev, curr = head, head.next
        while prev.next != head:
            if prev.val <= insertVal <= curr.val:
                break
            elif (prev.val > curr.val) and (insertVal > prev.val or insertVal < curr.val):
                break
            prev, curr = prev.next, curr.next

        node.next = curr
        prev.next = node
        return head
