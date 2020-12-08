class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.cnt = 0
        maxA = 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j):
            self.cnt += 1
            visited[i][j] = True
            for u,v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= u < m and 0 <= v < n and not visited[u][v] and grid[u][v]:
                    dfs(u, v)
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    pcnt = self.cnt
                    dfs(i, j)
                    maxA = max(maxA, self.cnt - pcnt)
                    # print(i, j, self.cnt, pcnt)
                
        return maxA