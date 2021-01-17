from statistics import median

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        xs, ys = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    xs.append(i)
                    ys.append(j)
        # find closest center
        x = median(xs)
        y = median(ys)
        # print(x, y)
        s = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    s += abs(x-i) + abs(y-j)
        return int(s)