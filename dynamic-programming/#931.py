class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        for i in range(1, n):
            for j in range(n):
                A[i][j] += min(A[i-1][max(j-1,0)], A[i-1][j], A[i-1][min(j+1,n-1)])
        return min(A[n-1])