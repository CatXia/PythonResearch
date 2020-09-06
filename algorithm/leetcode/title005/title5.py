class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ms = ""
        if len(s) > 0:
            ms = s[0]
        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                # 偶回文
                k = 1
                while i - k - 1 >= 0 and i + k <= len(s) - 1:
                    if s[i - k - 1] == s[i + k]:
                        k = k + 1
                    else:
                        break
                k = k - 1
                ts = s[i - k - 1:i + k + 1]
                if len(ms) < len(ts):
                    ms = ts
            if i > 0 and i + 1 < len(s) and s[i - 1] == s[i + 1]:
                # 奇回文
                k = 1
                while i - k - 1 >= 0 and i + k + 1 <= len(s) - 1:
                    if s[i - k - 1] == s[i + k + 1]:
                        k = k + 1
                    else:
                        break
                k = k - 1
                ts = s[i - k - 1:i + k + 1 + 1]
                if len(ms) < len(ts):
                    ms = ts
                    
        return ms
        