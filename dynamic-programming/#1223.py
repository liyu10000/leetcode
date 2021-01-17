class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        M = 10 ** 9 + 7
        # dp[l][d] means # of dice rolls of length l ending with d
        dp = [[0,0,0,0,0,0] for _ in range(n+1)]
        dp[1] = [1,1,1,1,1,1]
        for l in range(2, n+1):
            for d in range(6):
                if rollMax[d] >= l:
                    for d2 in range(6):
                        dp[l][d] += dp[l-1][d2]
                else:
                    for rm in range(1, rollMax[d]+1):
                        for d2 in range(6):
                            if d2 != d:
                                dp[l][d] += dp[l-rm][d2]
        return sum(dp[n]) % M