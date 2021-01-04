class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = (len(nums) - 1) // 2 # number of duplicates
        if n == 0:
            return nums[0]
        # index can only be 0, 2, 4, ..., 2*n
        i, j = 0, n
        while i <= j:
            k = (i + j) // 2
            k2 = k * 2
            if k2 == 0:
                return nums[0] if nums[k2] != nums[k2+1] else nums[2]
            if k2 == 2*n:
                return nums[k2]
            if nums[k2-1] == nums[k2]:
                j = k
            elif nums[k2] == nums[k2+1]:
                i = k + 1
            else:
                return nums[k2]
        return -1