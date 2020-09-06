class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n = 0
        isBeg = False
        isFS = False
        for i, v in enumerate(str):
            if not isBeg and v == " ":
                pass
            elif not isBeg and (v == "+" or v == "-"):
                if v == "-":
                    isFS = True
                isBeg = True
            elif v >= "0" and v <= "9":
                n = n * 10 + int(v)
                isBeg = True
            else:
                break
        if isFS:
            n = - n
        if n < - pow(2, 31):
            n = - pow(2, 31)
        if n > pow(2, 31) - 1:
            n = pow(2, 31) - 1
        return n
