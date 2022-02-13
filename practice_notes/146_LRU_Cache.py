"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
 Otherwise, add the key-value pair to the cache.
 If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv_pair = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.kv_pair:
            return -1
        self.kv_pair.move_to_end(key)
        return self.kv_pair[key]

    def put(self, key: int, value: int) -> None:
        if key in self.kv_pair:
            self.kv_pair.move_to_end(key)
        self.kv_pair[key] = value
        if len(self.kv_pair) > self.capacity:
            self.kv_pair.popitem(last=False)


class DLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _add_node(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _rmv_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        self._rmv_node(node)
        self._add_node(node)

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = DLinkedNode(key, value)
            self.size += 1
            if self.size > self.capacity:
                tail = self.tail.prev
                del self.cache[tail.key]
                self._rmv_node(tail)
                self.size -= 1
            self._add_node(new_node)
            self.cache[key] = new_node
