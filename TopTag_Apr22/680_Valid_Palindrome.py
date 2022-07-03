"""
680. Valid Palindrome II (E, 261)
"""

# what we know
# input - s: str
# only allow to delete at most one character from it

# for palindrome, we can use 2 pointers and start from both ends of the string
# if they're the same, increment lower pointer and decrement higher pointer
# else - we need to remove one of the 2 characters at current pointers
# and we don't know which one we should remove...
# can we use the function itself recursively?

def valid_palindrome(s: str) -> bool:
    def is_palindrome(start: int, end: int) -> bool:
        # substring from index start to end is palindrome
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            # we found a mismatch
            # test skipping i or skipping j
            return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)
            # alternatively
            # skip_i = s[i+1:j+1]
            # skip_j = s[i:j]
            # return skip_i == skip_i[::-1] or skip_j == skip_j[::-1]
        i += 1
        j -= 1
    return True

# follow up
# if instead of 1 delete, you're allow n delete
# abcaedba

def valid_palindrome_n(s: str, n: int) -> bool:
    # use backtracking
    valid = False

    def backtrack(start, end, k):
        if start == end and k >= 0:
            nonlocal valid
            valid = True
            return
        if s[start] == s[end]:
            backtrack(start + 1, end - 1, k)
        elif k == 0:
            return
        else:
            backtrack(start + 1, end, k - 1)
            backtrack(start, end - 1, k - 1)

    backtrack(0, len(s) - 1, n)
    return valid 