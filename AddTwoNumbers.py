# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        initial = True
        while l1 or l2 or carry:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            carry_, insert = divmod(l1.val + l2.val + carry, 10)
            carry = carry_
            if initial:
                result0 = ListNode(insert)
                result.next = result0
                initial = False
            else:
                result1 = ListNode(insert)
                result0.next = result1
                result0 = result1
            l1, l2 = l1.next, l2.next
        return result.next
