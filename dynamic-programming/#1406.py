# Min-Max solution
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        self.n = n
        self.backSum = [0] * n
        self.intMax = 2 ** 31 - 1
        self.intMin = - 2 ** 31
        self.dp = [self.intMin] * n
        self.backSum[-1] = stoneValue[-1]
        for i in range(n-2, -1, -1):
            self.backSum[i] = self.backSum[i+1] + stoneValue[i]

        Alice = self.helper(stoneValue, 0, 3)
        Bob = sum(stoneValue) - Alice
        # print(self.dp)
        if Alice > Bob:
            return 'Alice'
        elif Alice == Bob:
            return 'Tie'
        else:
            return 'Bob'
        
    def helper(self, stoneValue, i, M):
        if i >= self.n:
            return 0
        # if i >= self.n - M:
        #     return self.backSum[i]
        if self.dp[i] != self.intMin:
            return self.dp[i]
        curMin = self.intMax
        for x in range(1, M+1):
            # print(i, x)
            curMin = min(curMin, self.helper(stoneValue, i+x, M))
        self.dp[i] = self.backSum[i] - curMin
        return self.dp[i]