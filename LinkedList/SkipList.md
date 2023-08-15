# Skip List
Skip list is a data structure that sacrifice some level of space complexity for the ability to Insert, Search, Delete elements from a sorted set in `O(logN)` time. 

## Use Case/Examples
- Gaming Leader Board
- Moving Medians
- Concurrent Priority Queues with less lock contention/lock free

## General Idea
Create multiple layers of `Linked List`, which represent all or a subset of set elements, each linked list is sorted. 

At level 0, all elements of the sorted set is included. A probability `p` is given during initiation, to determine the probability of each element being 'copied' to high levels. As a result, during Search and Delete, we would search from the top of the levels, and expected to have `O(logN)` time complexity. 

```
N = Number of elements in set
p = probability of extending each element i in the next level
Expected Number of Levels = Log(1/p)(N)
```

### Initiation
To initiate a Skip List, we need to first define `Node` for linked list at each level of the skip list. 

```
class Node: 
    def __init__(self, val, max_lvl): 
        self.val = val
        self.next = [None] * (max_lvl + 1)
```

Noted, `Node.next` indicates the next pointers of the linked list node, at different levels of linked list in the skip list. `Node.next[0]` is the next pointer of node at level 0, for example.

```
class SkipList:
    def __init__(self, max_lvl, p): 
        self.max_lvl, self.p = max_lvl, p
        self.level = 0
        self.header = Node(-1, self.max_lvl)
```

### Insertion
During insertion, the program follows these logics for a new element with value `val`: 
1. Initiate an array `insert_point` of size `max_lvl + 1` to keep track of the insertion point of `val` at each level
2. Start from the top level, find `prev` node such that `prev.val < val AND (prev.next is None or prev.next >= val)` at each level `l`. Assign `insert_point[l] = prev` 
3. Create new node `node = Node(val, max_lvl)`
4. Use random number generator to determine `rlvl`, number of levels `node` should be copied to
5. Based on `rlvl`, initiate new levels as needed
6. Insert `node` from level 0 to level `rlvl` based on the insertion point in `inerst_point` at each level

Pseudo Code
```
def randomLvl(self): 
    lvl = 0
    while lvl < self.max_lvl + 1 and random.random() < self.p: 
        lvl += 1
    return lvl

def insert(self, val): 
    insert_point = [None] * (self.max_lvl + 1)
    curr = self.header
    for level in range(self.level, -1, -1): 
        # iterate all existing levels
        while curr.next[level] and curr.next[level].val < val: 
            curr = curr.next[level]
        # found insertion point
        insert_point[level] = curr
    rlvl = self.randomLvl()
    node = Node(val, rlvl)
    if rlvl > self.level:
        # initiate new levels as needed
        for l in range(self.level + 1, rlvl + 1): 
            insert_point[l] = self.head
        self.level = rlvl
    # insert node from level 0 to rlvl
    for l in range(rlvl): 
        node.next[l] = insert_point[l].next[l]
        insert_point[l].next[l] = node
```

### Search and Deletion
To take advantage of the multi-level linked list, we can start our search at the top most level for `search_val`

1. Iterate through each level `l` from `self.level` (current top level)
2. Initiate a `curr` pointer as `self.head[self.level]` at the beginning
3. Iterate horizontally across `l`, until `curr.next[l].val >= search_val or curr.next[l] is None`
4. If `curr.next[l].val == search_val`, FOUND VALUE, break loop and finish. Else, carry `curr` pointer to the `l-1`, repeat step 3. 
5. After level 0 is searched, then `search_val` is not in set. 

Pseudo Code
```
def search(self, search_val):
    curr = self.header
    for l in range(self.level, -1, -1): 
        while curr.next[l] and curr.next[l].val < search_val: 
            curr = curr.next[l]
        if curr.next[l].val == search_val: 
            break
    return l if curr.next[l].val == search_val else None
```

Once `search_val` is found at a level, all subsequent levels (lower than current level), will have `search_val` node. Thus, additional steps for deletion:

1. Initiate `pivot` array with length `self.level + 1`
2. for each level from level to 0, search the node prior to `search_val`, assign to `pivot[l]` if `search_val` exists
3. for each level from 0 to lvl, while applicable, use `pivot` to remove `search_val` node
4. remove and update `self.level` as needed

Psuedo Code
```
def erase(self, val):
    pivot = [None] * (self.level + 1)
    curr = self.header
    for l in range(self.level, -1, -1): 
        if curr.next[l] and curr.next[l] < val: 
            curr = curr.next[l]
        pivot[l] = curr
    curr = curr.next[0]
    if curr and curr.val == val: 
        for l in range(self.level + 1):
            if pivot[l].next[l].val != val: 
                break
            pivot[l].next[l] = curr.next[l]
    while self.level > 0 and self.header[self.level] is None:
        self.level -= 1
```