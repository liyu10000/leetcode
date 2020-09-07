class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0 for _ in range(n)]
        dp[0] = A[0]
        for i in range(1, n):
            m = 0
            for j in range(i-K, i):
                if j >= 0:
                    m = max(m, dp[j]+max(A[j+1:i+1])*(i-j))
                else:
                    m = max(m, max(A[:i+1])*(i+1))
            dp[i] = m
        # print(dp)
        return dp[-1]