class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, newi = 0, 0
        while i < len(nums):
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            nums[newi] = nums[i]
            newi += 1
            i += 1
        nums = nums[:newi]
        return newi