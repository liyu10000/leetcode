class Solution:
    def totalMoney(self, n: int) -> int:
        base = 28
        weeks, days = n // 7, n % 7
        weekMoney = base * weeks + 7 * (weeks - 1) * weeks // 2
        dayMoney = (days + 1) * days // 2 + weeks * days
        return weekMoney + dayMoney