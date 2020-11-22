# dp[i] records the maximum if nums[i] is taken
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                for j in range(i-1):
                    dp[i] = max(dp[i], nums[i]+dp[j])
            # print(i, dp)
        return max(dp[-2:])

# dp[i] records the maximum up to ith num
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            # print(i, dp)
        return dp[-1]