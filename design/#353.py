class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.w = width
        self.h = height
        self.f = food
        self.i = 0    # index of food to be eaten
        self.n = len(food) # number of food
        self.s = 0    # score
        self.ps = [[0,0]]  # blocks occupied by snake
        self.ds = {'U':[-1, 0], 'L':[0, -1], 'R':[0, 1], 'D':[1, 0]}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        r, c = self.ps[-1]
        r, c = r + self.ds[direction][0], c + self.ds[direction][1]
        # check if collides with border
        if r < 0 or r == self.h or c < 0 or c == self.w:
            return -1
        # check if finds food
        if self.i < self.n and r == self.f[self.i][0] and c == self.f[self.i][1]:
            self.ps.append([r, c])
            self.i += 1
            self.s += 1
        else:
            self.ps.pop(0)
            # check if collides with self
            l = len(self.ps)
            for i in range(l-1):
                if r == self.ps[i][0] and c == self.ps[i][1]:
                    return -1
            self.ps.append([r, c])
        return self.s