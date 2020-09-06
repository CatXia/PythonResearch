class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            lx = x
            n = 0
            while x > 0:
                n = 10 * n + x % 10
                x = x // 10
            return n == lx