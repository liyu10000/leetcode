class Solution:
    def numberOfWays(self, num_people: int) -> int:
        M = 10 ** 9 + 7
        dp = [0 for _ in range(num_people+1)]
        dp[0] = 1
        for n in range(2, num_people+1, 2):
            if n == 2:
                dp[n] = 1
            else:
                # 0 and i shakes hand
                for i in range(1, n, 2):
                    dp[n] += dp[i-1] * dp[n-i-1]
            dp[n] = dp[n] % M
        # print(dp)
        return dp[num_people]