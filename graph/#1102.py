# brute force backtracking, get TLE
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        
        def backtrack(i, j, minVal):
            if i == m-1 and j == n-1:
                self.maxVal = max(self.maxVal, minVal)
                return
            for u, v in [(i-1, j), (i, j+1), (i, j-1), (i+1, j)]:
                if 0 <= u < m and 0 <= v < n and not visited[u][v]:
                    visited[u][v] = 1
                    backtrack(u, v, min(minVal, A[u][v]))
                    visited[u][v] = 0
        
        self.maxVal = 0
        visited[0][0] = 1
        backtrack(0, 0, A[0][0])
        return self.maxVal

# union-find, add max value each time and check connectivity
class DisjointSet:
    def __init__(self, N):
        self.parents = list(range(N))
    
    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        self.parents[self.find(i)] = self.find(j)

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda c:A[c[0]][c[1]], reverse=True)
        visited = [[0 for j in range(n)] for i in range(m)]
        dsu = DisjointSet(m*n)
        for i, j in cells:
            visited[i][j] = 1
            for u, v in [(i-1, j), (i, j+1), (i, j-1), (i+1, j)]:
                if 0 <= u < m and 0 <= v < n and visited[u][v]:
                    dsu.union(i*n+j, u*n+v)
            if dsu.find(0) == dsu.find(m*n-1):
                return A[i][j]
        return -1