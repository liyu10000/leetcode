class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0:
                return n
            nums[n-1] *= -1
        return 0