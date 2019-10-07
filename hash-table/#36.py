class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = 9, 9
        for i in range(m):
            a = set()
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in a:
                        return False
                    else:
                        a.add(board[i][j])
        for i in range(m):
            a = set()
            for j in range(n):
                if board[j][i] != '.':
                    if board[j][i] in a:
                        return False
                    else:
                        a.add(board[j][i])
        for i in range(3):
            for j in range(3):
                a = set()
                for ii in range(3*i, 3*(i+1)):
                    for jj in range(3*j, 3*(j+1)):
                        if board[ii][jj] != '.':
                            if board[ii][jj] in a:
                                return False
                            else:
                                a.add(board[ii][jj])
        return True