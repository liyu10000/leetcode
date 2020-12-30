class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, maxProfit = float('inf'), 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minp = 2 ** 31
        diff = 0
        for i in range(1, n):
            minp = min(minp, prices[i-1])
            diff = max(diff, prices[i] - minp)
        return diff

# Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur, res = 0, 0
        for i in range(1, len(prices)):
            cur += prices[i] - prices[i-1]
            cur = max(0, cur)
            res = max(cur, res)
            print(i, cur, res)
        return res