"""
1249. Minimum Remove to Make Valid Parentheses (Medium, 294)
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""

# what we know
# input - s: str
# s has '(' and ')' and letters
# balance '(' and ')'

# for any given substring
# more '(' than ')': '((())(())' -> '((())' and '(())'
# more ')' than '(': '((())))(()'

# do we know if there's a limit for the length of s?
# do we remove the extra parentheses in place or not?
from collections import deque



def min_remove_parentheses(s: str) -> str:
    """
    time: O(n) - 2 time passes + join to make output = 3n -> n
    space: O(n) - to store tmp n
    :param s:
    :return:
    """
    num_open = 0
    unmatched_open = 0
    tmp = []
    # remove all unmatched ')'
    for ele in s:
        if ele == '(':
            num_open += 1
            unmatched_open += 1
        elif ele == ')':
            if unmatched_open == 0:
                # this ')' does not have a matching '('
                continue
            unmatched_open -= 1
        tmp.append(ele)

    # remove unmatched '('
    matched_open = num_open - unmatched_open
    ans = []
    for ele in tmp:
        if ele == '(':
            if matched_open == 0:
                continue
            matched_open -= 1
        ans.append(ele)
    return ''.join(ans)

def min_remove_parentheses1(s: str) -> str:
    """
    time: O(n) - 2 passes + stack to set (n) + final join (n) = 4n -> n
    space: O(n) - for stack and closed_rmv 2n -> n
    :param s:
    :return:
    """
    closed_rmv = set()
    stack = deque()
    for i, ele in enumerate(s):
        if ele == '(':
            stack.append(i)
        elif ele == ')':
            if not stack:
                closed_rmv.add(i)
            else:
                stack.pop()
    to_be_rmv = closed_rmv.union(set(stack)) if stack else closed_rmv
    ans = []
    for i, e in enumerate(s):
        if i not in to_be_rmv:
            ans.append(e)
    return ''.join(ans)
