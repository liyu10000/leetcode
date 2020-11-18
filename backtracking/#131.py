class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # build dp table
        dp = [[0]*n for _ in range(n)]
        for l in range(1, n+1):
            if l == 1:
                for i in range(n):
                    dp[i][i] = 1
            elif l == 2:
                for i in range(n-1):
                    dp[i][i+1] = 1 if s[i] == s[i+1] else 0
            else:
                for i in range(n-l+1):
                    dp[i][i+l-1] = 1 if (dp[i+1][i+l-2] and s[i] == s[i+l-1]) else 0
        # print(dp)
        # backtrack to collect answer
        self.ans = []
        self.backtrack(s, dp, 0, n, [])
        return self.ans
    
    def backtrack(self, s, dp, i, n, cur):
        if i == n:
            self.ans.append(cur)
            return
        for j in range(i, n):
            if dp[i][j]:
                self.backtrack(s, dp, j+1, n, cur+[s[i:j+1]])