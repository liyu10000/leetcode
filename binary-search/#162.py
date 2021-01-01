# O(n) time complexity
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        for i in range(n):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return 0
            elif i == n-1:
                if nums[i-1] < nums[i]:
                    return n-1
            else:
                if nums[i-1] < nums[i] > nums[i+1]:
                    return i
        return -1

# O(logn)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [-2**32] + nums + [-2**32]
        i, j = 1, n
        while i <= j:
            m = (i + j) // 2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m - 1
            if nums[m-1] > nums[m]:
                j = m - 1
            else:
                i = m + 1
        return 0

# O(logn)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n-1
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[m+1]:
                j = m
            else:
                i = m + 1
        return i