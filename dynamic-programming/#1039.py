class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for j in range(n)] for i in range(n)]
        MAX = 1e6
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if l == 3:
                    dp[i][j] = A[i] * A[i+1] * A[i+2]
                else:
                    dp[i][j] = MAX
                    for k in range(i+1, j):
                        # if k == i+1:
                        #     dp[i][k] = A[i] * A[k] * A[j]
                        # elif k == j-1:
                        #     dp[k][j] = A[i] * A[k] * A[j]
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i]*A[k]*A[j])
        print(dp)
        return dp[0][n-1]