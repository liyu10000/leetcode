# time limit exceeded
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += n
        return self.helper(d)
    
    def helper(self, d):
        if len(d) <= 1:
            return sum(list(d.values()))
        if len(d) == 2:
            keys = list(d.keys())
            if abs(keys[0] - keys[1]) == 1:
                return max(list(d.values()))
            else:
                return sum(list(d.values()))
        maxsum = 0
        for n in d:
            tmpd = d.copy()
            del tmpd[n]
            if n-1 in tmpd:
                del tmpd[n-1]
            if n+1 in tmpd:
                del tmpd[n+1]
            maxsum = max(maxsum, d[n]+self.helper(tmpd))
        return maxsum

# again, TLE
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] += n
        return self.helper(d)
    
    def helper(self, d):
        if len(d) <= 1:
            return sum(list(d.values()))
        presum = 0
        ns = list(d.keys())
        for n in ns:
            if n-1 not in d and n+1 not in d:
                presum += d[n]
                del d[n]
        maxsum = 0
        for n in d:
            tmpd = d.copy()
            del tmpd[n]
            if n-1 in tmpd:
                del tmpd[n-1]
            if n+1 in tmpd:
                del tmpd[n+1]
            maxsum = max(maxsum, d[n]+self.helper(tmpd))
        return presum + maxsum

# dp solution
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = defaultdict(int)
        for n in nums:
            d[n] += n
        keys = list(d.keys())
        keys.sort()
        dp = [0 for _ in range(len(keys))]
        dp[0] = d[keys[0]]
        for i in range(1, len(keys)):
            if keys[i] == keys[i-1] + 1:
                if i == 1:
                    dp[i] = max(d[keys[i]], dp[i-1])
                else:
                    dp[i] = max(dp[i-1], d[keys[i]]+dp[i-2])
            else:
                dp[i] = dp[i-1] + d[keys[i]]
        return dp[-1]