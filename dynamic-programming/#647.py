class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        for l in range(1, n+1):
            if l == 1:
                for i in range(n):
                    dp[i][i] = 1
            elif l == 2:
                for i in range(n-l+1):
                    dp[i][i+1] = 1 if s[i] == s[i+1] else 0
            else:
                for i in range(n-l+1):
                    dp[i][i+l-1] = 1 if dp[i+1][i+l-2] and s[i] == s[i+l-1] else 0
        # print(dp)
        return sum([sum(dp[i]) for i in range(n)])