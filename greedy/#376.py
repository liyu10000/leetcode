class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        m = 0
        i = 0
        while i < len(nums)-1:
            if nums[i] < nums[i+1]:
                while i < len(nums)-1 and nums[i] <= nums[i+1]:
                    i += 1
                m += 1
            elif nums[i] > nums[i+1]:
                while i < len(nums)-1 and nums[i] >= nums[i+1]:
                    i += 1
                m += 1
            else:
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                    i += 1
        return m + 1