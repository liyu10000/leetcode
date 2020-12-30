class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [0] * n  # dp[i] denotes profit gains from subsequence [0, i]
        for i in range(1, n):
            # case1: sell ith stock
            for j in range(i): # buy jth stock
                dp[i] = max(dp[i], dp[max(j-2, 0)]+prices[i]-prices[j])
            # case2: don't sell or buy ith stock
            dp[i] = max(dp[i], dp[i-1])
        # print(dp)
        return dp[n-1]