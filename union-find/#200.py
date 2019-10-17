class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    if self.isIsland(grid, i, j, m, n, visited):
                        count += 1
        
        return count
    
    def isIsland(self, grid, i, j, m, n, visited):
        visited[i][j] = True
        flag = True # true if is island
        for x,y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and not visited[x][y]:
                if not self.isIsland(grid, x, y, m, n, visited):
                    flag = False # note flag here does not do much, what really matters is the visited matrix
        return flag
        

# solution removing flag
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.isIsland(grid, i, j, m, n, visited)
                    count += 1
        
        return count
    
    def isIsland(self, grid, i, j, m, n, visited):
        visited[i][j] = True
        for x,y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1' and not visited[x][y]:
                self.isIsland(grid, x, y, m, n, visited)
