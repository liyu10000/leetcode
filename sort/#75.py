class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        curr = 0
        while curr < len(nums):
            if nums[curr] == 0 and curr > left:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
            elif nums[curr] == 2 and curr < right:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1