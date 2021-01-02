class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)
        # dp[i][j] refers to longest commen prefix subarray of A[i:] and B[j:]
        dp = [[0 for j in range(n2)] for i in range(n1)]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if i == n1-1 or j == n2-1:
                    dp[i][j] = 1 if A[i] == B[j] else 0
                else:
                    dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
        # print(dp)
        return max(max(dp[i]) for i in range(n1))

# add one more dimension to avoid border check
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n1, n2 = len(A), len(B)
        # dp[i][j] refers to longest commen prefix subarray of A[i:] and B[j:]
        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                dp[i][j] = dp[i+1][j+1] + 1 if A[i] == B[j] else 0
        # print(dp)
        return max(max(dp[i]) for i in range(n1))