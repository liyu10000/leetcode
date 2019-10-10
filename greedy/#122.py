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