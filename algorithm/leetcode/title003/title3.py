class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bInx, mLan, sMap = 0, 0, {}
        for i, v in enumerate(s):
            if v in sMap and sMap[v] >= bInx:
                if mLan < i - bInx:
                    mLan = i - bInx
                bInx = sMap[v] + 1
            elif i == len(s) - 1 and i - bInx + 1 > mLan:
                mLan = i - bInx + 1
            sMap[v] = i
        return mLan