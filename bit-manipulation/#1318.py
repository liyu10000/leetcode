class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        while a > 0 or b > 0 or c > 0:
            ai = a % 2
            bi = b % 2
            ci = c % 2
            if ci == 0:
                cnt += ai + bi
            else:
                if ai == 0 and bi == 0:
                    cnt += 1
            a //= 2
            b //= 2
            c //= 2
        return cnt