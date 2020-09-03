class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for _ in range(n)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-2], dp[i-1])
        return min(dp[n-2], dp[n-1])

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f1 = cost[0]
        f2 = cost[1]
        for i in range(2, n):
            f = cost[i] + min(f1, f2)
            f1, f2 = f2, f
        return min(f1, f2)