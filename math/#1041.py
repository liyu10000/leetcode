class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # north = 0, east = 1, south = 2, west = 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # Initial position is in the center
        x = y = 0
        # facing north
        idx = 0
        
        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]
        
        # after one cycle:
        # robot returns into initial position
        # or robot doesn't face north
        return (x == 0 and y == 0) or idx != 0