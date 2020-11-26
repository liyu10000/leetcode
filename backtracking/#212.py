class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        for word in words:
            if self.exist(board, word):
                res.append(word)
        return res        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        w = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, m, n, i, j, 1, w, word, {(i,j)}):
                        return True
        return False
    
    def dfs(self, board, m, n, i, j, s, w, word, visited):
        if s == w:
            return True
        for ii,jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= ii < m and 0 <= jj < n and not (ii,jj) in visited and board[ii][jj] == word[s]:
                visited.add((ii, jj))
                if self.dfs(board, m, n, ii, jj, s+1, w, word, visited):
                    return True
                visited.remove((ii, jj))
        return False