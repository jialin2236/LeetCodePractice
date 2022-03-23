# Recursion
**Recursion** is an approach to solving problems using a function that calls itself as a subroutine. 

## Properties
1. a simple base case (act as a terminating scenario, does not use recursion to produce an answer), is crucial in
   avoiding an infinite loop
2. a set of rules, recurrence relation (reduces other cases towards the base case)

## Recursion Function Guideline
let *F(x)* be the function, *X* be the function's input space.
1. Break the problem down into smaller scopes, `x_0, x_1, ... , x_n belong to X`
2. Call function *F(x_0), F(x_1), ... , F(x_n)* recursively to solve the subproblems of X
3. process the results from the recursive function calls to solve the problem corresponding to *X*

## Complexity
### Time
1. number of recursion invocations *R*
2. complexity of calculation that incurs along with each recursion call *O(s)*
```
O(T) = R * O(s)
```

#### Execution Tree
a tree (n-ary tree) to denote the execution flow of a recursive function.  
*each Node*: one invocation of the recursive function.
```
R = total number of nodes in the tree
```

### Space
1. recursion related pace
2. non-recursion related space

#### Recursion Related Space
memory cost that is incurred directly by the recursion, 
i.e. the stack to keep track of recursive function calls. 

For recursive algorithms, the function calls chain up successively until they reach a base case (a.k.a. bottom case). 
This implies that the space that is used for each function call is accumulated.

#### non-recursion related space
typically includes the space (normally in heap) that is allocated for the global variables.

## Examples
### Reverse String (344 - Easy)
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
```
def reverseString(s: List[str]) -> None:
    def helper(i, j): 
        if i >= j: 
           return 
        s[i], s[j] = s[j], s[i]
        helper(i + 1, j - 1)
    
    helper(0, len(s) - 1)
```

### Swap Nodes in Pairs (24 - Medium)
Given a linked list, swap every two adjacent nodes and return its head. 

You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

```
# ListNode -> ListNode.val, ListNode.next

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]: 
    def helper(node): 
       if not node or not node.next: 
         return node
       new_head = node.next
       next_seq = new_head.next
       new_head.next = node
       node.next = helper(next_seq)
       return new_head
    
    return helper(head)
```

### Fibonacci Number / Climbing Stairs (509/70 - Easy)
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is 
the sum of the two preceding ones, starting from 0 and 1.

Given `n`, calculate `F(n)`

```
def fib(n: int) -> int: 
   cache = {}
   
   def helper(num):
      if num in cache: 
         result = cache[num]
      else: 
         if num < 2: 
            result = num
         else: 
            result = helper(num - 1) + helper(num - 2)
         cache[num] = result
      return result
   
   return helper(n)
```
