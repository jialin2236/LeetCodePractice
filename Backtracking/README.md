# Backtracking
Backtracking is a technique typically used when a problem asks us to enumerate all feasible 
solutions. It recurse on partial feasible solutions, and stops when it reaches the end of 
the search space, and append a feasible solution to the answer. 

Backtracking could follow the following template of code: 
```
search_space = [SOME DEFINED SPACE GIVEN BY PROBLEM]
answer = []
def backtrack(index, partial_solution): 
    # we've reached the end of the search space / achieve a qualify solution
    if index == len(search_space) or partial_solution is qualified:
        # NOTE: it's EXTREMELY important to append the COPY of the partial_solution,
        # otherwise at the end it'd point it to the original value, which is empty (meaningless) 
        answer.append(partial_solution.copy())
        return
    for candidate in list_of_candidates_from_search_space: 
        if candidate is feasible:
            partial_solution.append(candidate)
            backtrack(index + 1, partial_solution)
            partial_solution.pop()
```
Time Complexity: Exponential

Space Complexity: N