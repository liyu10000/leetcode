class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        while l <= h:
            m = (h - l) // 2 + l
            g = guess(m)
            if g == 0:
                return m
            elif g > 0:
                l = m + 1
            else:
                h = m - 1
        return m