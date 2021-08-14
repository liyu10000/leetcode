class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        rows, cols = len(board), len(board[0])
        op_clr = 'W' if color == 'B' else 'B'
        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for rStep, cStep in directions:
            op_cnt = 0
            r, c = rMove, cMove
            while True:
                r += rStep
                c += cStep
                if 0 <= r < rows and 0 <= c < cols:
                    if board[r][c] == op_clr:
                        op_cnt += 1
                    elif board[r][c] == color:
                        if op_cnt > 0:
                            return True
                        else:
                            break
                    else:
                        break
                else:
                    break
        return False
                    