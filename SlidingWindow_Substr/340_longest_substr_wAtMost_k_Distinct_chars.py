"""
Given a string s and an integer k, return the length of the longest substring of s
that contains at most k distinct characters.
"""

"""
Loop through the string, start with a window size of 1, expand when number of unique chars 
is within range (<= k), slide window to the right, when number of unique chars exceeds k. 
s = 'aabbcc', k = 3 
"""
from collections import OrderedDict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n == 0 or k == 0:
            return 0
        left = right = 0
        max_len = 1
        count = {}
        while right < n:
            char_i = s[right]
            if char_i not in count:
                count[char_i] = 0
            count[char_i] += 1
            right += 1  # right pointer will move rightward regardless of next step (slide/expand)

            while len(count) > k:  # there are more than k unique characters in the window, slide window
                char_l = s[left]
                count[char_l] -= 1  # decrement character count of char at left pointer
                if count[char_l] == 0:
                    del count[char_l]
                left += 1  # left pointer move rightward (right pointer already did)

            # update max_len as needed
            max_len = max(max_len, right - left)
        return max_len

    def lengthOfLongestSubstringKDistinct1(self, s: str, k: int) -> int:
        n = len(s)
        if s * k == 0:
            return 0
        left = right = 0
        # dictionary to look up if char had appeared
        max_len = 1
        hashmap = OrderedDict()

        while right < n:
            character = s[right]
            # if character is already in the hashmap -
            # delete it, so that after insert it becomes
            # the rightmost element in the hashmap
            if character in hashmap:
                del hashmap[character]
            hashmap[character] = right
            right += 1

            # slidewindow contains k + 1 characters
            if len(hashmap) == k + 1:
                # delete the leftmost character
                _, del_idx = hashmap.popitem(last=False)
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstringKDistinct("abaccc", 2))

