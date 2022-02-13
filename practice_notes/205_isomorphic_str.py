"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters
in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters.

No two characters may map to the same character,
but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def transform(st):
            new_st = []
            mapping = {}

            for i in range(len(st)):
                st_i = st[i]
                if st_i not in mapping:
                    mapping[st_i] = i
                new_st_i = mapping[st_i]
                new_st.append(new_st_i)

        return transform(s) == transform(t)

    def isIsomorphic0(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        map0, map1 = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 not in map0) and (c2 not in map1):
                map0[c1] = c2
                map1[c2] = c1
            elif map0.get(c1) != c2 or map1.get(c2) != c1:
                return False
        return True 