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

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:       
        INT_MAX = 2**31
        n = len(arr)
        dp = [[INT_MAX] * n for _ in range(n)]
        for l in range(1, n+1):
            if l == 1:
                for left in range(n):
                    dp[left][left] = 0
            for left in range(0, n-l+1):
                right = left + l - 1
                for i in range(left, right):
                    dp[left][right] = min(dp[left][right], dp[left][i] + dp[i+1][right] + max(arr[left:i+1]) * max(arr[i+1:right+1]))
        # print(dp)
        return dp[0][n-1]