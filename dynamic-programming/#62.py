# recursive but time consuming
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

# O(m*n) in time and space
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [[1] * m for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                a[i][j] = a[i-1][j] + a[i][j-1]
        return a[n-1][m-1]

