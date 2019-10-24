# first try: time limit exceeded
class Solution:
    def __init__(self):
        self.count = 0
        
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        def helper(s):
            if len(s) == 0 or (len(s) == 1 and int(s[0]) != 0):
                self.count += 1
            else:
                if int(s[0]) != 0 and int(s[1]) != 0:
                    helper(s[1:])
                if 10 <= int(s[:2]) <= 26:
                    helper(s[2:])

        helper(s)
        return self.count


# second try: 
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        
        dp = [0] * (n + 1)
        if s[n-1] != '0':
            dp[n-1] = 1
        dp[n] = 1 # dp[n] is auxiliary
        
        for i in range(n-2, -1, -1):
            one = s[i]
            two = s[i: i+2]
            if '1' <= one <= '9':
                dp[i] = dp[i+1]
            if '10' <= two <= '26':
                dp[i] += dp[i+2]
                
        return dp[0]