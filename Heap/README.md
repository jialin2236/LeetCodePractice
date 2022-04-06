# Heap
## Definition and Classification
**Heap** is a special type of binary tree that meets the following criteria: 
1. it's a complete binary tree
2. the value of each node must be no greater than (or no less than) the value of its child nodes

### Complexity
|           |  Time  | Space  |
| ---       | ---    | ---    |
| Construction |  `O(N)`  |  `O(N)`  |
| Insertion | `O(logN)` |  `O(1)`  |
| Deletion  | `O(logN)` |  `O(1)`  |
| pop       | `O(1)`    |  `O(1)`  |


### Classification
max heap: a node's value >= child nodes' value

min heap: a node's value <= child nodes' value 

## Operations
### Insertion
1. check if it's a complete binary tree
2. node and child node value comparison
3. insert new value to the next empty spot (to maintain a complete binary tree)
4. check inserted node value with its parent
   if min/max property does not hold: swap node with its parent, move pointer to parent and
   repeat process until check passes (heapify)

### Deletion
removing the "top" element from the heap, and maintain the property of the heap (min/max). 
1. determine if it's a complete binary tree
2. value of each node <= (>=) to its child nodes
3. replace the top element with the last element in the tree
4. remove the last element
5. check min/max property, swap current top element with max/min of it's children (heapify)

### Array to Tree properties
given a node's index `i` 
1. its two children `lc = 2*i + 1` and `rc = 2*i + 2`
2. its parent `parent = (i - 1) // 2`
3. if `i > n / 2`, it's a leaf node

## Pseudo Code
### Construct(Heapify)
implement by hand 
```
class heap:
   def __init__(self, nums: List[int]): 
      self.arr = nums
      
   def heapify_node(self, idx, j):
      lc, rc = 2idx + 1, 2idx + 2
      target_i = idx
      if lc <= j and self.arr[lc] < self.arr[target_i]: 
         target_i = lc
      if rc <= j and self.arr[rc] < self.arr[target_i]:
         target_i = rc
      if target_i != idx: 
         self.arr[target_i], self.arr[idx] = self.arr[idx], self.arr[target_i]
         self.heapify_node(target_i, j)
      
   def heapify() -> None:
      n = len(self.arr) - 1
      i = (n - 1)//2
      while i >= 0: 
         self.heapify_node(i, n)
         i -= 1
```
python class
```
import heapq

heapq.heapify(arr)
```

### Insertion to heap
implement by hand
```
# in class heap defined above

def insert_heap(self, val: int) -> None: 
   i = len(self.arr) 
   self.arr.append(val)
   parent = (i - 1) // 2
   self.heapify_node(parent, len(arr))
```
python class 
```
heapq.heappush(arr, val)
```

### Pop top element
implement by hand
```
# in class heap defined above

def heap_pop(self) -> int: 
   self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
   self.heapify(0, len(arr) - 2)
   return self.arr.pop()
```
in python class
```
heapq.heappop(arr)
```