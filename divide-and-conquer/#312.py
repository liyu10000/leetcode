class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [n for n in nums if n > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        for l in range(2, n):
            for i in range(n-l):
                j = i + l
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j])
        return dp[0][n-1]