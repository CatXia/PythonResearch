import re
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        v = re.match(p, s)
        return v != None and v.group(0) == s