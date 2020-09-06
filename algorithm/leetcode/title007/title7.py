class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = 0
        isZS = x > 0
        if not isZS:
            x = - x
        while x > 0:
            n = n * 10 + x % 10
            x = x // 10
        if not isZS:
            n = - n
        if n < -pow(2, 31) or n > pow(2, 31) - 1:
            return 0
        return n