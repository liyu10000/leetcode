# count each row and column
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            counts = 0
            for j in range(n):
                if grid[i][j]:
                    counts += 1
            if counts > 1:
                ans += counts
                # set server with a different label
                for j in range(n):
                    if grid[i][j]:
                        grid[i][j] = 2
        # print(grid)
        for j in range(n):
            counts = 0
            toadd = 0
            for i in range(m):
                if grid[i][j]:
                    counts += 1
                    if grid[i][j] == 1:
                        toadd += 1
            if counts > 1:
                ans += toadd
        # print(grid)
        return ans

# store row and column counts
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rSum = [sum(grid[i]) for i in range(m)]
        cSum = [sum([grid[i][j] for i in range(m)]) for j in range(n)]
        print(rSum, cSum)
        return sum(rSum[i]+cSum[j] > 2 for i in range(m) for j in range(n) if grid[i][j])

# more concise solution
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rSum, cSum = list(map(sum, grid)), list(map(sum, zip(*grid)))
        return sum(rSum[i]+cSum[j] > 2 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])