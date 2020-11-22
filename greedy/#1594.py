class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minps = [[None] * n for _ in range(m)]
        minps[0][0] = grid[0][0]
        maxps = [[None] * n for _ in range(m)]
        maxps[0][0] = grid[0][0]
        for i in range(1, m):
            minps[i][0] = minps[i-1][0] * grid[i][0]
            maxps[i][0] = maxps[i-1][0] * grid[i][0]
        for j in range(1, n):
            minps[0][j] = minps[0][j-1] * grid[0][j]
            maxps[0][j] = maxps[0][j-1] * grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                ps = [minps[i-1][j] * grid[i][j], 
                      maxps[i-1][j] * grid[i][j], 
                      minps[i][j-1] * grid[i][j], 
                      maxps[i][j-1] * grid[i][j]]
                minps[i][j] = min(ps)
                maxps[i][j] = max(ps)
                # print(i, j, grid[i][j], products[i][j])
        maxp = maxps[m-1][n-1]
        if maxp < 0:
            maxp = -1
        elif maxp > 0:
            maxp %= (10 ** 9 + 7)
        return maxp