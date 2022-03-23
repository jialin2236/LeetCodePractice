"""
206. Reverse Linked List (easy)
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        def helper(node):
            if not node.next or not node:
                nonlocal new_head
                new_head = node
                return
            post = node.next
            helper(post)
            post.next = node
            node.next = None

        helper(head)
        return new_head

    def reverse_list_iter(self, head:Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev