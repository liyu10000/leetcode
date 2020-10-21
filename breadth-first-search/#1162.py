# naive brute force search, get TLE
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        # traverse the grid to find all ones
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i,j])
        # print(queue)
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        # start bfs
        dist = [[n*2] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    for u,v in queue:
                        dist[i][j] = min(dist[i][j], abs(i-u)+abs(j-v))
        # get the biggest distance
        maxd = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    maxd = max(maxd, dist[i][j])
        return maxd


# real BFS
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        # traverse the grid to find all ones
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i,j])
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        # start bfs
        maxd = 0
        while queue:
            # print(queue)
            maxd += 1
            newqueue = []
            for i,j in queue:
                for u,v in [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]:
                    if 0 <= u < n and 0 <= v < n and grid[u][v] == 0:
                        grid[u][v] = maxd
                        newqueue.append([u,v])
            queue = newqueue
        return maxd - 1