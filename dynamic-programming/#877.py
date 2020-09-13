# recursive, TLE
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        s = self.stone(piles, 0, len(piles)-1)
        return s > sum(piles) - s

    def stone(self, piles, i, j):
        if j == i + 1:
            return max(piles[i], piles[i+1])
        pickfirst = piles[i] + self.stone(piles, i+1, j) 
        picklast = self.stone(piles, i, j-1) + piles[j]
        return max(pickfirst, picklast)

# dp
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # use dp[i][j] to indicate the stones Alex wins over Lee from i to j of the piles (piles[i:j+1])
        # dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = piles[i]
        for d in range(1, n):
            for i in range(n - d):
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        return dp[0][-1] > 0