class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        MAX = 365000
        dp = [0] * n
        dp[0] = min(costs)
        for i in range(1, n):
            d1 = dp[i-1]
            d7 = MAX
            d30 = MAX
            j = i - 1
            while j >= 0 and days[i] - days[j] < 7:
                j -= 1
            d7 = min(d7, dp[j])
            j = i - 1
            while j >= 0 and days[i] - days[j] < 30:
                j -= 1
            d30 = min(d30, dp[j])
            dp[i] = min(d1+costs[0], d7+costs[1], d30+costs[2])
        # print(dp)
        return dp[n-1]