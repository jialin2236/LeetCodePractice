# Search Topics
## Binary Search
This [LeetCode article](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems) 
provides an extremely thorough analysis of binary search, with a comprehensive template, 
binary search's use case, as well as a number of problems as examples. 

### When to Use? 
splits the search space into two halves and only keep the half that has the search target and throw away the 
other half that would not possibly have the answer. 

#### Typical given conditions: 
1. an array
2. some condition (integers?) that creates a constraint(s), making some scenario not feasible
3. a task to find min/max of a solution that satisfies all constraint(s)

Complexity: 

- Time: O(logN)
- Space: O(1)

Usage: 
1. given an array to be searched (sorted or not)
2. if we can discover a search sapce, and some kind of monotonicity. 
For example, if `condition(k) is True` then `condition(k+1) is True`, then we can consider binary search

### Key things to pay attention to
- when to exit the loop? `left < right` or `left <= right`
- how to initialize the boundary variables `left` and `right`
- how to update the boundary? choosing between `left = mid`, `left = mid + 1` and `right = mid`, `right = mid - 1`

### Template
```
def binary_search(space) -> int: 
    def condition(value) -> bool: 
        pass
    
    left, right = min(search_space), max(search_space)
    while left < right: 
        mid = left + (right - left) // 2
        # alternatively
        # mid = right - (right - left) // 2
        if condition(mid): 
            right = mid
            # left = mid 
        else: 
            left = mid + 1
            # right = mid - 1
    return left
```
