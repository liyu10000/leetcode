# use extra space
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, w = 0, 0, 0
        tmp = [0] * (m+n)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                tmp[w] = nums1[i]
                i += 1
            else:
                tmp[w] = nums2[j]
                j += 1
            w += 1
        while i < m:
            tmp[w] = nums1[i]
            i += 1
            w += 1
        while j < n:
            tmp[w] = nums2[j]
            j += 1
            w += 1
        for i in range(m+n):
            nums1[i] = tmp[i]

# write from the end
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, w = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                i -= 1
            else:
                nums1[w] = nums2[j]
                j -= 1
            w -= 1
        while j >= 0:
            nums1[w] = nums2[j]
            j -= 1
            w -= 1