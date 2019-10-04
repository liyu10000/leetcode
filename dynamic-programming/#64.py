class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                    continue
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                    continue
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]