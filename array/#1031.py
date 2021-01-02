class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        # calculate prefix sum
        n = len(A)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i+1] = preSum[i] + A[i]
        # calculate moving max sum M subarray, from left and from right
        Mleft = [0] * n
        for i in range(n-M+1):
            if i == 0:
                Mleft[i] = preSum[M]
            else:
                Mleft[i] = max(Mleft[i-1], preSum[i+M] - preSum[i])
        Mright = [0] * n
        for i in range(n-M, -1, -1):
            if i == n-M:
                Mright[i] = preSum[n] - preSum[i]
            else:
                Mright[i] = max(Mright[i+1], preSum[i+M] - preSum[i])
        # for each case of L-length subarray, find max M subarray
        res = 0
        for i in range(n-L+1):
            Lsum = preSum[i+L] - preSum[i]
            Mlsum, Mrsum = 0, 0
            if i >= M: # left
                Mlsum = Mleft[i-M]
            if i + L <= n - M: # right
                Mrsum = Mright[i+L]
            res = max(res, Lsum+Mlsum, Lsum+Mrsum)
        return res