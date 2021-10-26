class Solution(object):
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x > 2**31 or x < -2**31 or x == 0:
            pass
        else:
            x_str_list = list(str(x))
            if x_str_list[0] == '-':
                rev_list = ['-'] + x_str_list[1:][::-1]
            else:
                rev_list = x_str_list[::-1]
            rev = int(''.join(rev_list))
        return rev

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x > 2**31 or x < -2**31 or x == 0:
            pass
        else:
            neg = abs(x)/x
            x = abs(x)
            while x > 0:
                x, rx_i = divmod(x,10)
                rev = rx_i + rev*10
            rev = int(neg*rev)
        return rev
