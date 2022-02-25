"""
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
Medium 

"""
import collections
from typing import Optional

class Node: 
    def __init__(self, val: Optional[int]):
        self.val = val
        self.next = None
        self.random = None


"""
Questions: 
could there be nodes with same value but different pointers?
does only the last node have its next point to None? 
what do we care more, space or time? 
Thoughts: 
1. we can traverse through the linked list and copy nodes as we go
2. go back to head and traverse again to build the random pointer
--- this approach would require O(2N) time and O(N) space, since we need to 
create a hash table to store the nodes for second step
Alternatively, we can create a hashtable as traverse, and construct next and random 
at the same time. Time: O(N), Space: O(N)
"""
class Solution: 
    def copy_random_list(head: Optional[Node]): 
        # Time: O(N), Space: O(N)
        # create a place holder for the copy node, default it to a node with value 0
        copy = collections.defaultdict(lambda x: Node(0)) 
        copy[None] = Node(None) # add list ending
        curr = head
        while curr: 
            # create the copy of node curr, and update its val, next, random with
            # actual value of curr, placeholder copy of curr.next and placeholder 
            # copy of curr.random
            copy[curr].val = curr.val
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = head.next
        return copy[head]

    def copy_random_list1(head: Optional[Node]): 
        # A -> B -> C
        # insert copied node as the next node of its original, and copied nodes
        # next to be original node's next
        # A' as copy of A, A -> A' -> B -> B'
        curr = head
        while curr: 
            copy_node = Node(curr.val)
            copy_node.next = curr.next
            curr.next = copy_node
        # for random pointer, a copied node points to original node's 
        # random pointer's next
        # A.random = C and C -> C'
        # A'.random = C' (C.next)
        curr = head
        while curr: 
            copy_node = curr.next
            copy_node.random = curr.random.next if curr.random else None
            curr = curr.next.next # move to the next copy node
        copy = head.next
        old = head
        new_head = head.next
        # A -> A' -> B -> B' -> C -> C'
        while copy:
            copy.next = copy.next.next if copy.next else None
            old.next = old.next.next
            copy = copy.next
            old = old.next.next
        return new_head
