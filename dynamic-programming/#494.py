# brute force, get TLE
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        
        def helper(i, t):
            if i == n:
                return t == 0
            return helper(i+1, t+nums[i]) + helper(i+1, t-nums[i])
        
        return helper(0, S)

# dp
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        dp = [[0] * 2001 for _ in range(n)]
        dp[0][nums[0]+1000] = 1
        dp[0][-nums[0]+1000] += 1
        for i in range(1, n):
            for s in range(-1000, 1001):
                if dp[i-1][s+1000] > 0:
                    dp[i][s+nums[i]+1000] += dp[i-1][s+1000]
                    dp[i][s-nums[i]+1000] += dp[i-1][s+1000]
        return 0 if S > 1000 else dp[n-1][S+1000]