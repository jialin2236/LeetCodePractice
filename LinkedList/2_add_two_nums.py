"""
2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_nums_i(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        ans0 = ListNode()
        ans = ans0
        carry = 0
        while l1 and l2:
            curr = l1.val + l2.val + carry
            carry, curr_d = divmod(curr, 10)
            ans0.next = ListNode(curr_d)
            l1, l2 = l1.next, l2.next
            ans0 = ans0.next
        l1 = l2 if l2 else l1
        while l1:
            curr = l1.val + carry
            carry, curr_d = divmod(curr, 10)
            ans0.next = ListNode(curr_d)
            l1 = l1.next
            ans0 = ans0.next
        if carry:
            ans0.next = ListNode(carry)
        return ans.next

    def add_nums_util(self, l1: Optional[ListNode], l2: Optional[ListNode], ans: Optional[ListNode], carry: int) -> None:
        if not (l1 or l2 or carry):
            return
        if not (l1 or l1) and carry:
            ans.next = ListNode(carry)
            return
        if l1 or l2:
            if not carry and not (l1 and l2):
                l1 = l2 if l2 else l1
                ans.next = l1
                return
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum_i = v1 + v2 + carry
            carry_i, digit_i = divmod(sum_i, 10)
            ans.next = ListNode(digit_i)
            n1 = l1.next if l1 else None
            n2 = l2.next if l2 else None
            self.add_nums_util(n1, n2, ans.next, carry_i)

    def add_nums(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans0 = ListNode()
        ans = ans0
        self.add_nums_util(l1, l2, ans0, 0)
        return ans.next
