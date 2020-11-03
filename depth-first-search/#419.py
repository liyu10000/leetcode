# DFS, the same as the solution to 'Unique Islands'
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        m = len(board)
        n = len(board[0])
        count = 0
        self.visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and not self.visited[i][j]:
                    self.dfs(board, m, n, i, j)
                    count += 1
        return count
    
    def dfs(self, board, m, n, i, j):
        self.visited[i][j] = True
        for u,v in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= u < m and 0 <= v < n and board[u][v] == 'X' and not self.visited[u][v]:
                self.dfs(board, m, n, u, v)


# only count the upper-left 'X'
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        m = len(board)
        n = len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.'):
                    count += 1
        return count