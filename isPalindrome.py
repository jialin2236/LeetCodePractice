# 9. Palindrome Number
class Solution(object):
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n_dig = int(math.log10(x)) + 1
        h_ndig, o_dig = divmod(n_dig,2)
        x0, x1 = divmod(x, 10**h_ndig)
        if o_dig == 1:
            x0 = divmod(x0, 10)[0]
        x1_ = 0
        while x1 > 0:
            x1, r_ = divmod(x1,10)
            x1_ = r_ + 10*x1_
        if x1_ == x0:
            return True
        else:
            return False

    def isPalindrome2(self, x):
        x1 = 0
        while x > x1 > 0:
            x, x1_ = divmod(x, 10)
            x1 = x1_ + 10*x1
        if x == x1 or x == int(x1/10):
            return True
        return False
