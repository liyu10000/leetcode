class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        steps = 0
        queue = [(0, 0)]
        visited = {(0, 0)}
        while queue:
            newqueue = []
            for i, j in queue:
                if i == x and j == y:
                    return steps
                for u, v in [(i+2, j+1), (i+1, j+2), (i-1, j+2), (i-2, j+1), (i-2, j-1), (i-1, j-2), (i+1, j-2), (i+2, j-1)]:
                    if not (u, v) in visited:
                        visited.add((u, v))
                        newqueue.append((u, v))
            queue = newqueue
            steps += 1
        return steps