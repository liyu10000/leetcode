# recursive, get TLE
class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 2:
            return n
        k = int(n**0.5)
        mmin = n
        for i in range(2, k+1):
            mmin = min(mmin, 1+self.numSquares(n-i**2))
        return mmin

# recursive with memorization
class Solution:
    mem = {0:0, 1:1, 2:2}
    
    def numSquares(self, n: int) -> int:
        if n in self.mem:
            return self.mem[n]
        k = int(n**0.5)
        mmin = n
        for i in range(2, k+1):
            nn = n-i**2
            if nn in self.mem:
                cnt = self.mem[nn]
            else:
                cnt = self.numSquares(nn)
                self.mem[nn] = cnt
            mmin = min(mmin, 1+cnt)
        return mmin


