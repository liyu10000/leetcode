class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        right = 0
        lasti = 0
        jumps = 0
        for i in range(n-1):
            right = max(right, i+nums[i])
            if lasti == i:
                jumps += 1
                lasti = right
        return jumps