class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])
        while True:
            flag1, marks1 = self.horizontalSearch(board, m, n)
            flag2, marks2 = self.verticalSearch(board, m, n)
            flag = flag1 or flag2
            if flag:
                self.updateBoard(board, marks1, marks2, m, n)
            else:
                break
        return board

    def horizontalSearch(self, board, m, n):
        # search by rows
        marks = [[1 for j in range(n)] for i in range(m)]
        flag = False
        for i in range(m):
            # forward
            for j in range(1, n):
                if board[i][j] > 0 and board[i][j] == board[i][j-1]:
                    marks[i][j] = marks[i][j-1] + 1
            # print(i, marks[i])
            # backward
            j = n - 1
            while j >= 0:
                if marks[i][j] > 2:
                    flag = True
                    prevj = j
                    j -= marks[i][j]
                    for tmpj in range(prevj, j, -1):
                        marks[i][tmpj] = 1
                else:
                    marks[i][j] = 0
                    j -= 1
            # print(i, marks[i])
        # print(marks)
        return flag, marks    

    def verticalSearch(self, board, m, n):
        # search by columns
        marks = [[1 for j in range(n)] for i in range(m)]
        flag = False
        for j in range(n):
            # forward
            for i in range(1, m):
                if board[i][j] > 0 and board[i][j] == board[i-1][j]:
                    marks[i][j] = marks[i-1][j] + 1
            # print(j, [marks[i][j] for i in range(m)])
            # backward
            i = m - 1
            while i >= 0:
                if marks[i][j] > 2:
                    flag = True
                    previ = i
                    i -= marks[i][j]
                    for tmpi in range(previ, i, -1):
                        marks[tmpi][j] = 1
                else:
                    marks[i][j] = 0
                    i -= 1
            # print(j, [marks[i][j] for i in range(m)])
        # print(marks)
        return flag, marks

    def updateBoard(self, board, marks1, marks2, m, n):
        # update by columns
        for j in range(n):
            r, w = m-1, m-1 # read, write
            while r >= 0:
                if marks1[r][j] == 0 and marks2[r][j] == 0:
                    board[w][j] = board[r][j]
                    w -= 1
                r -= 1
            while w >= 0:
                board[w][j] = 0
                w -= 1
        # print(board)