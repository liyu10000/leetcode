class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:       
        INT_MAX = 2**31
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                if l == 1:
                    dp[i][j] = arr[i] * arr[j]
                else:
                    dp[i][j] = INT_MAX
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], max(arr[i:k+1]) * max(arr[k+1:j+1]) + dp[i][k] + dp[k+1][j])
        # print(dp)
        return dp[0][n-1]