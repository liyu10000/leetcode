class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sn, tn = len(s), len(t)
        dp = [[0 for j in range(tn+1)] for i in range(sn+1)]
        # for j in range(tn+1):
        #     dp[0][j] = 0
        for i in range(sn+1):
            dp[i][0] = 1
        for i in range(1, sn+1):
            for j in range(1, tn+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[sn][tn]