# backtracking, get TLE
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        self.mcost = 20 * n
        colorAlter = {0:[1,2], 1:[0,2], 2:[0,1]}
        
        # backtrack
        def backtrack(i, colori, cost):
            if i == n:
                self.mcost = min(self.mcost, cost)
                return
            for nexti in colorAlter[colori]:
                backtrack(i+1, nexti, cost+costs[i][colori])
        
        backtrack(0, 0, 0)
        backtrack(0, 1, 0)
        backtrack(0, 2, 0)
        return self.mcost

# dp
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        colorAlter = {0:[1,2], 1:[0,2], 2:[0,1]}
        dp = [[0,0,0] for _ in range(n)]
        dp[0] = costs[0]
        
        for i in range(1, n):
            for colori in [0,1,2]:
                prev1, prev2 = colorAlter[colori]
                dp[i][colori] = min(dp[i-1][prev1], dp[i-1][prev2]) + costs[i][colori]
        
        return min(dp[n-1])