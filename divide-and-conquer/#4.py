class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        middle = (m + n) // 2 + 1
        count = 0
        x, y = 0, 0
        while count < middle:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    x, y = y, nums1[i]
                    i += 1
                else:
                    x, y = y, nums2[j]
                    j += 1
            elif i < m:
                x, y = y, nums1[i]
                i += 1
            else:
                x, y = y, nums2[j]
                j += 1
            count += 1
        if (m + n) % 2 == 0:
            return (x + y) / 2
        else:
            return y