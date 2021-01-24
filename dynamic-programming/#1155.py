class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        MAX = 10 ** 9 + 7
        
        def helper(d, t):
            if d == 0:
                return 1 if t == 0 else 0
            if (d,t) in memo:
                return memo[(d,t)]
            s = 0
            for tt in range(max(0, t-f), t):
                s += helper(d-1, tt)
            s = s % MAX
            memo[(d,t)] = s
            return s
        
        return helper(d, target)