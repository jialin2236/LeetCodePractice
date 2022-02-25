"""
173. Binary Search Tree Iterator
Medium

Implement the BSTIterator class that represents an iterator over the
in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class.
The root of the BST is given as part of the constructor.
The pointer should be initialized to a non-existent number smaller than any element in the BST.

boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer,
otherwise returns false.

int next() Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number,
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid.
That is, there will be at least a next number in the in-order traversal when next() is called.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTIterator_stack: 
    def __init__(self, root):
        self.stack = deque()
        self.traverse_left(root)

    def traverse_left(self, node):
        if node.left: 
            self.stack.append(node.left)
            node = node.left

    def next():
        top = self.stack.pop()
        if top.right: 
            self.traverse_left(top.right)
        return top.val

    def has_next(): 
        return self.stack == deque()


class BSTIterator: 
    def __init__(self, root):
        self.inorder = deque()
        self._inorder(root)

    def _inorder(self, node):
        if node: 
            self._inorder(node.left)
            self.inorder.append(node)
            self._inorder(node.right)

    def next():
        top = self.inorder.popleft()
        return top.val

    def has_next():
        return len(self.inorder) > 0

