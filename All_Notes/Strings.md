## KMP string matching
It's used for substring (pattern) matching between 2 given strings (`s.find(subs)`), in **linear time**. 

I found this [blog post](http://jakeboxer.com/blog/2009/12/13/the-knuth-morris-pratt-algorithm-in-my-own-words/) 
to be the most intuitive

### Pattern Table
Throughout different documentations I found various reference on how this could be interpreted/understood.
The more intuitive explanation for me, is to understand it similar to a dynamic programming (memoization)
table (list in this case). It is 
```
for list of proper prefix of given string s up till index i, 
and list suffix up till the same index, the longest matching substring
e.x.
s = 'abababca', i = 4 -> substr = 'ababa' 
list of proper prefix = ['a', 'ab', 'aba', 'abab']
list of proper suffix = ['a', 'ba', 'aba', 'baba']
-> 3 
i = 7, proper suffix has to have 'c', there is no proper prefix with 'c', -> 0
i = 8, first letter matches ('a'), no match for i = 7, -> 1

pattern table of s = [0, 0, 1, 2, 3, 4, 0, 1]
```

### Use the Pattern Table
If a partial match of length `k` is found, and `table[k] > 1`, we can skip ahead `k - table[k - 1]`
characters. 

```
e.x. matching 'abababca' against 'bacbababaabcbab'
char: | a | b | a | b | a | b | c | a |
idx:  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
val:  | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |

1st match 
bacbababaabcbab 
 |
 abababca
length of match k = 1, table[k - 1] = 0, no skip

2nd match
bacbababaabcbab
    |||||
    abababca
length of match k = 5, table[k - 1] = 3, skip ahead k - table[k-1] = 5 - 3 = 2 chars
bacbababaabcbab
    xx|||
      abababca

length of match k = 3, table[k - 1] = 1, skip ahead k - table[k-1] = 3 - 1 = 2 chars
bacbababaabcbab
    xxxx|
        abababca

pattern > remaining of string to match -> no match
```

### Implementation
```
def get_pattern_table(p): 
    lps = [0 for _ in range(len(p))]
    i, j = 1, 0
    while i < len(p): 
        if p[i] == p[j]:
            j += 1
            lps[i] = j
            i += 1
        else: 
            if j > 0: 
                j = lps[j-1]
            else: 
                i += 1
    return lps
    
def kmp(p, s): 
    m, n = len(s), len(p)
    i = j = 0
    table = lps(p)
    while i < m: 
        if s[i] == p[j]: 
            i += 1
            j += 1
        if j == n: 
            return i - n
        if i < m and s[i] != p[j]: 
            if j > 0: 
                j = lps[j-1]
            else: 
                i += 1 
```