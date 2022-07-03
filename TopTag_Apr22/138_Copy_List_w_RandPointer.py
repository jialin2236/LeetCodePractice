"""
138. Copy List with Random Pointer (M, 70)
"""
from typing import Optional

class Node:
    def __init__(self, x):
        self.val = int(x)
        self.next = None
        self.random = None

# construct a deep copy of the list
# n brand new nodes
# return head

# use hash table

class Solution:
    def copy_random_list_hash(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return

        copy = {head: Node(head.val)}
        curr = head
        while curr:
            curr_copy = copy[curr]
            nxt, rnd = curr.next, curr.random
            if nxt and nxt not in copy:
                copy[nxt] = Node(nxt.val)
            if rnd and rnd not in copy:
                copy[rnd] = Node(rnd.val)
            curr_copy.next = copy.get(nxt, None)
            curr_copy.random = copy.get(rnd, None)
            curr = curr.next
        return copy[head]

    # use interweaving linked list
    # insert copy of node to node.next, copy.next to be node's original next
    def copy_random_list_inplace(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return

        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            copy.random = curr.random.next if curr.random else None

        new_head = head.next
        old_curr, new_curr = head, head.next
        while old_curr:
            old_curr.next = new_curr.next
            new_curr.next = new_curr.next.next if new_curr.next else None
            old_curr = old_curr.next
            new_curr = new_curr.next
        return new_head