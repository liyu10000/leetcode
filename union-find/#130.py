class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for i in range(m)]
        to_flip = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    to_add = []
                    if self.dfs_inside(board, i, j, m, n, visited, to_add):
                        to_flip.extend(to_add)
                    
        for i, j in to_flip:
            board[i][j] = 'X'
        
        return board
    
    def dfs_inside(self, board, i, j, m, n, visited, to_add):
        if i <= 0 or i >= m-1 or j <= 0 or j >= n-1:
            return False
        
        visited[i][j] = True
        is_inside = True
        for x, y in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
            if board[x][y] == 'O' and not visited[x][y]:
                if not self.dfs_inside(board, x, y, m, n, visited, to_add):
                    is_inside = False
                
        if is_inside:
            to_add.append((i, j))
            return True
        else:
            return False
