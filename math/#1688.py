class Solution:
    def numberOfMatches(self, n: int) -> int:
        # return n - 1 # correct answer, winner needs to beat the rest
        c = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
                c += n
            else:
                n = (n-1) // 2 + 1
                c += n - 1
        return c