"""
23. Merge k Sorted Lists (Hard, 64 fb tagged 0 ~ 6 months)
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq

from LinkedList import LinkedNode
from typing import List, Optional

# example: [[1,4,5],[1,3,4],[2,6]]
# output: 1->1->2->3->4->4->5->6
# can we use a heap to store at most k elements, pop the smallest each time, and push the top element's next
# node into the heap

class Solution:
    def merge_k_list_h(self, lists: List[Optional[LinkedNode]]) -> Optional[LinkedNode]:
        """
        time: O(Nlogk) - every pop and insertion is O(logk), and we're doing it N times to insert and pop all N elements
        space: O(k)
        :param lists:
        :return:
        """
        val = [(node.val, i) for i, node in enumerate(lists)]
        heapq.heapify(val)
        head = LinkedNode(-1)
        curr = head
        while val:
            v, i = heapq.heappop(val)
            node = lists[i]
            lists[i] = node.next
            curr.next = node
            if lists[i]:
                heapq.heappush(val, (lists[i].val, i))
            curr = curr.next
        return head.next

    def merge_k_list_ms(self, lists: List[Optional[LinkedNode]]) -> Optional[LinkedNode]:
        # similar to merge sort
        def merge2lists(l1, l2):
            head = curr = LinkedNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1 or l2:
                curr.next = l1 if l1 else l2
            return head.next

        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = merge2lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if n > 0 else None