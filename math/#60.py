class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1]
        for i in range(1, n):
            fac.append(fac[-1]*i)
        
        res = ''
        nums = list(range(1, n+1))
        while n > 0:
            q, r = divmod(k-1, fac[n-1])
            res += str(nums[q])
            del nums[q]
            k = r+1
            n -= 1
        return res

# vallina backtracking, get TLE
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.s = ''
        self.k = k
        self.backtrack(n, 0, '', set())
        return self.s
        
    def backtrack(self, n, c, s, visited):
        if c == n:
            self.k -= 1
            if self.k == 0:
                self.s = s
            return
        for i in range(1, n+1):
            if not i in visited:
                visited.add(i)
                self.backtrack(n, c+1, s+str(i), visited)
                visited.remove(i)