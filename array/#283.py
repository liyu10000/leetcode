class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w = 0, 0
        n = len(nums)
        while r < n:
            if nums[r]:
                nums[w] = nums[r]
                w += 1
            r += 1
        while w < n:
            nums[w] = 0
            w += 1