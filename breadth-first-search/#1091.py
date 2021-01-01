# level-by-level search, get TLE
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        q = [(0,0)]
        steps = 0
        while q:
            steps += 1
            newq = []
            for i,j in q:
                if i == N-1 and j == N-1:
                    return steps
                grid[i][j] = -1 # mark as visited
                for u in range(i-1, i+2):
                    for v in range(j-1, j+2):
                        if 0 <= u < N and 0 <= v < N and (u != i or v != j) and grid[u][v] == 0:
                            newq.append((u, v))
            q = newq
            # print(q)
        return -1

# mark distance, don't create new queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        q = [(0,0)]
        grid[0][0] = 1
        while q:
            i, j = q.pop(0)
            dist = grid[i][j]
            if i == N-1 and j == N-1:
                return dist
            for u,v in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j+1), (i+1, j+1), (i+1, j), (i+1, j-1)]:
                if 0 <= u < N and 0 <= v < N and grid[u][v] == 0:
                    q.append((u, v))
                    grid[u][v] = dist + 1
            # print(q)
        return -1