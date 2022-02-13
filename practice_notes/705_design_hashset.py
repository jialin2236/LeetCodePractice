"""
705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Bucket_LinkedList:
    def __init__(self):
        self.head = Node(0)

    def insert(self, new_val):
        if not self.exists(new_val):
            new_node = Node(new_val)
            new_node.next = self.head.next
            self.head.next = new_node

    def delete(self, value):
        curr = self.head
        while curr.next:
            if curr.next.val == value:
                skip = curr.next.next
                curr.next = skip
                return
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Bucket_BST:
    def __init__(self):
        self.root = None

    def insert(self, root: Optional[BinaryTreeNode], value):
        if not root:
            return BinaryTreeNode(value)
        if value < root.val:
            root.left = self.insert(root.left, value)
        elif value == root.val:
            return root
        else:
            root.right = self.insert(root.right, value)
        return root

    def search(self, root: Optional[BinaryTreeNode], value):
        if not root or root.val == value:
            return root
        if value < root.val:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    def largest(self, root: Optional[BinaryTreeNode]):
        while root.right:
            root = root.right
        return root

    def smallest(self, root:Optional[BinaryTreeNode]):
        while root.left:
            root = root.left
        return root

    def delete(self, root: Optional[BinaryTreeNode], value) -> Optional[BinaryTreeNode]:
        if value < root.val:
            root.left = self.delete(root.left, value)
        if value > root.val:
            root.right = self.delete(root.right, value)
        else:
            if not (root.left or root.right):
                root = None
            if root.right:
                right_min = self.smallest(root.right).val
                root.val = right_min
                root.right = self.delete(root.right, right_min)
            else:
                left_max = self.largest(root.left).val
                root.val = left_max
                root.left = self.delete(root.left, left_max)
        return root

class MyHashSet:
    def __init__(self):
        self.key_range = 769
        self.bucket_link = [Bucket_LinkedList() for i in range(self.key_range)]
        self.bucket_bst = [Bucket_BST() for i in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def add(self, key):
        bucket_i = self._hash(key)
        self.bucket_link[bucket_i].insert(key)
        tree_i = self.bucket_bst[bucket_i]
        tree_i.insert(tree_i.root, key)


    def remove(self, key):
        bucket_i = self._hash(key)
        self.bucket_link[bucket_i].delete(key)
        tree_i = self.bucket_bst[bucket_i]
        tree_i.delete(tree_i.root, key)

    def contains(self, key):
        bucket_i = self._hash(key)
        self.bucket_link[bucket_i].exists(key)
        tree_i = self.bucket_bst[bucket_i]
        tree_i.search(tree_i.root, key)

