class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = x if x >= 0 else -x
        res = 0
        while x != 0:
            mod = x % 10
            x = x // 10
            res = res * 10 + mod
        res = res * sign
        if res > 2 ** 31 - 1 or res < - 2 ** 31:
            res = 0
        return res