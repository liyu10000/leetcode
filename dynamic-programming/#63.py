# first trial
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] == 1:
                        return 0
                    obstacleGrid[i][j] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if i == 0:
                    if obstacleGrid[i][j-1] == 0:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = 1
                elif j == 0:
                    if obstacleGrid[i-1][j] == 0:
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = 1
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]


