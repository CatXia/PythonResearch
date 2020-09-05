class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i
            if i < m and nums2[j-1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0:
                    ml = nums2[j-1]
                elif j == 0:
                    ml = nums1[i-1]
                else:
                    ml = max(nums1[i-1], nums2[j-1])

                if (m + n) % 2 == 1:
                    return ml

                if i == m:
                    mr = nums2[j]
                elif j == n:
                    mr = nums1[i]
                else:
                    mr = min(nums1[i], nums2[j])

                return (ml + mr) / 2.0