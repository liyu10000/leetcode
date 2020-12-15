class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # find all rotten oranges
        rotten = []
        fresh = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh = True
        if not rotten:
            return -1 if fresh else 0
        # bfs
        steps = -1
        while rotten:
            steps += 1
            newrotten = []
            for i,j in rotten:
                for u,v in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                    if 0 <= u < m and 0 <= v < n and grid[u][v] == 1:
                        newrotten.append((u,v))
                        grid[u][v] = 2
            rotten = newrotten
        # check for remaining fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return steps