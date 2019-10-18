class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for point in points:
            res.append(((point[0]**2+point[1]**2), point))
        res = sorted(res, key=lambda x:x[0])
        return [res[i][1] for i in range(K)]