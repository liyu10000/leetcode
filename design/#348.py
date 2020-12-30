class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.p1rows = [0] * n
        self.p1cols = [0] * n
        self.p1diag = [0, 0]
        self.p2rows = [0] * n
        self.p2cols = [0] * n
        self.p2diag = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.p1rows[row] += 1
            self.p1cols[col] += 1
            if row == col:
                self.p1diag[0] += 1
            if row + col == self.n-1:
                self.p1diag[1] += 1
            if self.p1rows[row] == self.n or self.p1cols[col] == self.n or self.p1diag[0] == self.n or self.p1diag[1] == self.n:
                return 1
        else:
            self.p2rows[row] += 1
            self.p2cols[col] += 1
            if row == col:
                self.p2diag[0] += 1
            if row + col == self.n-1:
                self.p2diag[1] += 1
            if self.p2rows[row] == self.n or self.p2cols[col] == self.n or self.p2diag[0] == self.n or self.p2diag[1] == self.n:
                return 2
        return 0