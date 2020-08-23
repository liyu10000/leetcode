class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    if matrix[i][j] == 1 and dp[i-1][j-1]*dp[i-1][j]*dp[i][j-1] > 0:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                    else:
                        dp[i][j] = matrix[i][j]
        return sum([sum(dp[i]) for i in range(m)])