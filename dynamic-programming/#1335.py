class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        elif d == n:
            return sum(jobDifficulty)
        elif d == 1:
            return max(jobDifficulty)
        dp = [[0] * n for _ in range(d+1)]
        MAX = 300 * 1000
        for i in range(1, d+1): # i days
            if i == 1:
                for j in range(n):
                    if j < i-1:
                        dp[i][j] = -1
                    else:
                        dp[i][j] = max(dp[i][j-1], jobDifficulty[j])
            else:
                for j in range(n): # jth job
                    if j < i-1:
                        dp[i][j] = -1
                    elif j == i-1:
                        dp[i][j] = dp[i-1][j-1] + jobDifficulty[j]
                    else:
                        dp[i][j] = MAX
                        for k in range(i-2, j): # finish jobs up to k in i-1 days
                            dp[i][j] = min(dp[i][j], dp[i-1][k] + max(jobDifficulty[k+1:j+1]))
        # print(dp)
        return dp[d][n-1]