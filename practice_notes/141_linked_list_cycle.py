"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously
following the next pointer.

Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

"""
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle0(self, head: Optional[ListNode]) -> bool:
        """
        time: O(n)
        space: O(n) - since it creates a set to track visited nodes
        :param head:
        :return:
        """
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        """
        slow: slow pointer that moves 1 step at a time
        fast: fast pointer that moves 2 steps at a time
        idea: slow and fast pointer will eventually meet if a cycle exists
        time: O(n+k) - k is the cyclic length
        space: 1
        :param head:
        :return:
        """
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
