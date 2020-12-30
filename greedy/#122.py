# first try
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit

# second try
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        while i < len(prices)-1:
            while i < len(prices)-1 and prices[i] > prices[i+1]:
                i += 1
            low = prices[i]
            while i < len(prices)-1 and prices[i] <= prices[i+1]:
                i += 1
            high = prices[i]
            profit += high - low
        return profit

# 2d dp, get TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for j in range(n)] for i in range(n)]
        for l in range(2, n+1):
            if l == 2:
                for i in range(n-1):
                    if prices[i+1] - prices[i] > 0:
                        dp[i][i+1] = prices[i+1] - prices[i]
            else:
                for i in range(n-l+1):
                    j = i + l - 1
                    for k in range(i+1, j):
                        dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j])
        return dp[0][n-1]