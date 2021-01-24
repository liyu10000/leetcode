# recursive, get TLE
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        memo = [[-1 for j in range(N)] for i in range(N)]
        
        def helper(k, r, c):
            if k == 0:
                return 1
            if k == 1 and memo[r][c] != -1:
                return memo[r][c]
            p = 0.0
            for nextr, nextc in [(r-1,c-2), (r-2,c-1), (r-2,c+1), (r-1,c+2), (r+1,c+2), (r+2,c+1), (r+2,c-1), (r+1,c-2)]:
                if 0 <= nextr < N and 0 <= nextc < N:
                    p += 1/8 * helper(k-1, nextr, nextc)
            if k == 1:
                memo[r][c] = p
            return p
        
        return helper(K, r, c)

# dp
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        memo = [[0.0 for j in range(N)] for i in range(N)]
        memo[r][c] = 1.0
        
        for k in range(K):
            memo2 = [[0.0 for j in range(N)] for i in range(N)]
            for r in range(N):
                for c in range(N):
                    for nextr, nextc in [(r-1,c-2), (r-2,c-1), (r-2,c+1), (r-1,c+2), (r+1,c+2), (r+2,c+1), (r+2,c-1), (r+1,c-2)]:
                        if 0 <= nextr < N and 0 <= nextc < N:
                            memo2[nextr][nextc] += memo[r][c] / 8.0
            memo = memo2
        
        return sum(map(sum, memo))