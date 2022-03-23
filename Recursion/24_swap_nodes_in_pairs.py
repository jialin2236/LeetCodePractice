"""
24. Swap Nodes in Pairs (Medium)
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
from typing import Optional

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def swap_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new_head = head.next
        next_seq = new_head.next
        new_head.next = head
        head.next = self.swap_nodes(next_seq)
        return new_head

    def swap_nodes_iter(self, head:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        prev.next = head
        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next
        return dummy.next