class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = dict()
        for idx, n in enumerate(nums):
            nother = target - n
            if nother in dc:
                return [dc[nother], idx]
            dc[n] = idx

