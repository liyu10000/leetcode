# RANSAC, but not very stable
import math
import random

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        p = 0.5  # good estimation
        v = 0.8  # probability of outliers
        m = 2  # minimum number of points to fit a line
        N = int(math.log(1 - p) / math.log(1 - (1 - v)**m))  # maximum number of iterations
        print(n, N)
        self.maxCnt = 0
        for i in range(N):
            self.ransac(points, n, m)
        return self.maxCnt
    
    def ransac(self, points, n, m):
        # randomly select m points for fitting a line
        basePoints = random.sample(range(n), m)
        print(basePoints)
        # solve for parameters of the model
        # can be solved by checking x1*y2 + x2*y3 + x3*y1 - x3*y2 - x2*y1 - x1 * y3 == 0
        # for details refer this link: https://math.stackexchange.com/questions/38338/methods-for-showing-three-points-in-mathbbr2-are-colinear-or-not
        x1, y1 = points[basePoints[0]]
        x2, y2 = points[basePoints[1]]
        # determine how many points
        cnt = 2
        for i in range(n):
            if not i in basePoints:
                if self.collinear(x1, y1, x2, y2, points[i]):
                    cnt += 1
        self.maxCnt = max(self.maxCnt, cnt)
        # reestimate line model with new inliers
        # since the model will be the same in this question, omit this step

    def collinear(self, x1, y1, x2, y2, point):
        x3, y3 = point
        return x1*y2 + x2*y3 + x3*y1 - x3*y2 - x2*y1 - x1 * y3 == 0



# brute force
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        maxCnt = 0
        for i in range(n-1):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cnt = 2
                if x1 == x2 and y1 == y2:
                    for k in range(n):
                        if k != i and k != j:
                            if points[k][0] == x1 and points[k][1] == y1:
                                cnt += 1
                else:                
                    for k in range(n):
                        if k != i and k != j:
                            if self.collinear(x1, y1, x2, y2, points[k]):
                                cnt += 1
                maxCnt = max(maxCnt, cnt)
        return maxCnt

    def collinear(self, x1, y1, x2, y2, point):
        x3, y3 = point
        return x1*y2 + x2*y3 + x3*y1 - x3*y2 - x2*y1 - x1 * y3 == 0