# modify nums array inplace
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if nums[i] > max:
                max = nums[i]

        return max

# without modification of original array
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxs = nums[0]
        currmax = nums[0]
        for i in range(1,len(nums)):
            currmax = max(nums[i], nums[i] + currmax)
            if currmax > maxs:
                maxs = currmax

        return maxs