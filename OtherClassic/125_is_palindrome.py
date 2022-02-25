class Solution(object):
    def reverse(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        sr = s
        while i < j:
            sr[i], sr[j] = s[j], s[i]
            i += 1
            j -= 1
        return sr

    def isPalindrome(self, s:str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        s_ = [i.lower() for i in s if i.isalnum()]
        n = len(s_)
        left = n//2
        right = left + 1 if n % 2 == 1 else left
        return s_[:left] == self.reverse(''.join(s_[right:]))

    def isPalindrome1(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    solve = Solution()
    ts = "0P"
    print(solve.isPalindrome(ts))