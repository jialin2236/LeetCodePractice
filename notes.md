# Notes for Data Structure
## Array and List 
`Arrays` are specially optimised for arithmetic computations so if you’re going to perform similar operations you should 
consider using an `array` instead of a `list`.

`List` can have elements of different data types, while array contain
elements of the same type. 

When we try the same operation (example: division) on a list, we get a TypeError because builtin python lists do not 
support the `__div__` protocol. It takes an extra step to perform this calculation on a list because then you’d have to
loop over each item one after the other and save to another list.

```
# Divide each element by a certain number
## Array
from numpy import array
cost = array([4,8,12,10,5,4,100])
cost_d2 = cost/2

cost_list = [4,8,12,10,5,4,100]
cost_list_d2 = [c/2 for c in cost_list]
```

## Hash Table 
Hashing is a technique or process of mapping keys, values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used.

Let a hash function `H(x)` maps the value `x` at the index `x%10` in an Array. For example if the list of values is [11,12,13,14,15] it will be stored at positions {1,2,3,4,5} in the array or Hash table respectively.

## Stack and Queue 
Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle. Queue is a container of objects (a linear collection) that are 
inserted and removed according to the first-in first-out (FIFO) principle.

Stack: `Deque` append and remove from the end. 

Queue: `Deque` append from the end and remove from the beginning. 

