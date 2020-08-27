class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and count[i] < count[j] + 1:
                    count[i] = count[j] + 1
        # print(count)
        return max(count)