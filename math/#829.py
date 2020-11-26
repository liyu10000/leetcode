# brute force, get TLE
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 1
        for i in range(1, N//2+1):
            roughj = int((2*N+i**2) ** 0.5)
            for j in range(roughj-3, roughj+4):
                if (i + j) * (j - i + 1) // 2 == N:
                    cnt += 1
                    break
        return cnt

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 0
        for d in range(1, N+1):
            residue = d * (d - 1) // 2
            nd = N - residue
            if nd <= 0:
                break
            if nd % d == 0:
                cnt += 1
        return cnt