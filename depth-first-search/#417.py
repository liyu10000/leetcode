class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        pvisited = [[False] * n for _ in range(m)]
        avisited = [[False] * n for _ in range(m)]
        self.directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        for i in range(m):
            self.dfs(matrix, pvisited, i, 0, m, n)
            self.dfs(matrix, avisited, i, n-1, m, n)
        for j in range(n):
            self.dfs(matrix, pvisited, 0, j, m, n)
            self.dfs(matrix, avisited, m-1, j, m, n)
        
        positions = []
        for i in range(m):
            for j in range(n):
                if pvisited[i][j] and avisited[i][j]:
                    positions.append([i, j])
        return positions
    
    def dfs(self, matrix, visited, i, j, m, n):
        visited[i][j] = True
        for d in self.directions:
            x = i + d[0]
            y = j + d[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, visited, x, y, m, n)