# dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = set(coins)
        MAX = 10e5
        dp = [MAX for _ in range(amount+1)]
        dp[0] = 0
        for a in range(1, amount+1):
            if a in coins:
                dp[a] = 1
            else:
                for c in coins:
                    if a-c > 0 and dp[a-c] != -1:
                        dp[a] = min(dp[a], 1 + dp[a-c])
                if dp[a] == MAX:
                    dp[a] = -1
        # print(dp)
        return dp[amount]

# recursive with memorization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {c:1 for c in coins}
        memo[0] = 0
        MAX = 2**31
        
        def helper(a):
            if a in memo:
                return memo[a]
            memo[a] = MAX
            for c in coins:
                if c < a:
                    memo[a] = min(memo[a], 1+helper(a-c))
            return memo[a]
    
        res = helper(amount)
        return res if res < MAX else -1