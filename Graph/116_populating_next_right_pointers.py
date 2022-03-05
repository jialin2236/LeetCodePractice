"""
116. Populating Next Right Pointers in Each Node (Medium)
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.

Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""
import collections
from typing import Optional


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect_q(self, root: Optional[Node]) -> Optional[Node]:
        """
        time: O(N) - traverse the entire tree
        space: O(N) - queue to maintain the traversal
        :param root:
        :return:
        """
        if not root:
            return root

        queue, prev = collections.deque(), None
        queue.append(root)
        queue.append(None)

        while queue:
            curr = queue.popleft()
            while curr:
                if prev:
                    prev.next = curr
                if curr.left:
                    queue.append(curr.left)
                    queue.append(curr.right)
                prev, curr = curr, queue.popleft()
            prev = curr
            if queue:
                queue.append(curr)

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        """
        if a node has node.next, the node's right child is the predecessor of node.next's left child
        time: O(N) - traverse the entire tree
        space: O(1)
        :param root:
        :return:
        """
        if not root:
            return

        head = root

        while head.left:
            pointer = head
            while pointer:
                pointer.left.next = pointer.right
                if pointer.next:
                    pointer.right.next = pointer.next.left
                pointer = pointer.next
            head = head.left
            