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