class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        s = sum(cardPoints)
        if n == k:
            return s
        ans = s
        winSum = sum(cardPoints[:n-k])
        for i in range(n-k, n):
            ans = min(ans, winSum)
            winSum -= cardPoints[i-n+k]
            winSum += cardPoints[i]
        ans = min(ans, winSum)
        return s - ans