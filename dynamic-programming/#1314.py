class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        m = len(mat)
        n = len(mat[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = mat[i][j]
                elif i == 0:
                    dp[i][j] = mat[i][j] + dp[i][j-1]
                elif j == 0:
                    dp[i][j] = mat[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = mat[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                left = j-K-1
                right = min(n-1, j+K)
                top = i-K-1
                bottom = min(m-1, i+K)
                a = dp[bottom][right]
                b = dp[bottom][left] if left >= 0 else 0
                c = dp[top][right] if top >= 0 else 0
                d = dp[top][left] if top >= 0 and left >= 0 else 0
                ans[i][j] = a - b - c + d 
                # ans[i][j] = dp[bottom][right] - dp[bottom][left] - dp[top][right] + dp[top][left]
        return ans

# add cushion to dp matrix
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        m = len(mat)
        n = len(mat[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = mat[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                left = max(j-K, 0)
                right = min(n, j+K+1)
                top = max(i-K, 0)
                bottom = min(m, i+K+1)
                ans[i][j] = dp[bottom][right] - dp[bottom][left] - dp[top][right] + dp[top][left]
        return ans