class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        # print(points[0])
        maxint = 0
        n = len(points)
        for i in range(n-1):
            maxint = max(maxint, points[i+1][0] - points[i][0])
        return maxint