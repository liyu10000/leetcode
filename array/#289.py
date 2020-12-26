class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        states = {2,  # live, live
                  3,  # live, dead
                  4,  # dead, live
                  5}  # dead, dead
        for i in range(m):
            for j in range(n):
                cnt = -board[i][j] # subtract self
                for u in range(i-1, i+2):
                    for v in range(j-1, j+2):
                        if 0 <= u < m and 0 <= v < n and 1 <= board[u][v] <= 3:
                            cnt += 1
                # print(i, j, cnt)
                if board[i][j] == 1:
                    if cnt == 2 or cnt == 3:
                        board[i][j] = 2
                    else:
                        board[i][j] = 3
                else:
                    if cnt == 3:
                        board[i][j] = 4
                    else:
                        board[i][j] = 5
        # print(board)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2 or board[i][j] == 4:
                    board[i][j] = 1
                else:
                    board[i][j] = 0