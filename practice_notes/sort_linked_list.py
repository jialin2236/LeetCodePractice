class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_val):
        if not self.head:
            self.head = Node(new_val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(new_val)

    def sorted_merge(self, a, b):
        result = None
        if not a:
            return b
        if not b:
            return a
        if a.val < b.val:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result

    def find_middle(self, h):
        if not h:
            return h
        slow = fast = h
        while slow.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self, h):
        if not h or not h.next:
            return h
        middle = self.find_middle(h)
        middle_p1 = middle.next
        middle.next = None
        left = self.merge_sort(h)
        right = self.merge_sort(middle_p1)
        ans = self.sorted_merge(left, right)
        return ans
