class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i, j = 0, 1
        while j < len(nums):
            if nums[i] == nums[j]:
                if j - i == 2:
                    del nums[j]
                else:
                    j += 1
            else:
                i = j
                j += 1
        return i + 2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i = 1
        for j in range(2, len(nums)):
            if nums[j] != nums[i] or nums[j] != nums[i-1]:
                i += 1
                nums[i] = nums[j]
        return i + 1