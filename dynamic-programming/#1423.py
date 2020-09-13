# recursive, TLE
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        p = self.pick(cardPoints, 0, len(cardPoints)-1, 0, k)
        return p
    
    def pick(self, cardPoints, i, j, n, k):
        if n == k:
            return 0
        pickfirst = cardPoints[i] + self.pick(cardPoints, i+1, j, n+1, k)
        picklast = cardPoints[j] + self.pick(cardPoints, i, j-1, n+1, k)
        return max(pickfirst, picklast)

# recursive, faster than the first one, but still TLE
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        self.dp = [[0 for _ in range(n)] for i in range(n)]
        for i in range(n):
            self.dp[i][i] = cardPoints[i]
        return self.pick(cardPoints, 0, n-1, 0, k)
    
    def pick(self, cardPoints, i, j, c, k):
        if c == k:
            return 0
        if self.dp[i][j] != 0:
            return self.dp[i][j]
        # print(i, j)
        pickfirst = cardPoints[i] + self.pick(cardPoints, i+1, j, c+1, k)
        picklast = cardPoints[j] + self.pick(cardPoints, i, j-1, c+1, k)
        self.dp[i][j] = max(pickfirst, picklast)
        return self.dp[i][j]

# using sliding window, but brute force sum, TLE
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s = sum(cardPoints)
        if n == k:
            return s
        ans = 0
        for i in range(k+1):
            ans = max(ans, s - sum(cardPoints[i:i+n-k]))
            # print(ans)
        return ans