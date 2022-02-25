# Backtracking
Backtracking is a technique typically used when a problem asks us to enumerate all feasible 
solutions. It recurse on partial feasible solutions, and stops when it reaches the end of 
the search space, and append a feasible solution to the answer. 

Backtracking could follow the following template of code: 
```
search_space = [SOME DEFINED SPACE GIVEN BY PROBLEM]
answer = []
def backtrack(index, partial_solution): 
    # we've reached the end of the search space
    if index == len(search_space): 
        answer.append(partial_solution)
        return
    for candidate in list_of_candidates_from_search_space: 
        if candidate is feasible:
            partial_solution.append(candidate)
            backtrack(index + 1, partial_solution)
            partial_solution.pop()
```
Time Complexity: Exponential

Space Complexity: N