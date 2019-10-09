import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend is 0 or divisor is 0: 
            return 0
        total = dividend/divisor
        if total > 0:
            return min(math.floor(total), 2147483647)
        if total < 0:
            return max(math.ceil(total), - 2147483648)