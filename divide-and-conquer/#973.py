# sort
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for point in points:
            res.append(((point[0]**2+point[1]**2), point))
        res = sorted(res, key=lambda x:x[0])
        return [res[i][1] for i in range(K)]

# use heap
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dists = [p[0]**2+p[1]**2 for p in points]
        q = []
        for i, (p,d) in enumerate(zip(points, dists)):
            heapq.heappush(q, [d, i])
        res = []
        while K:
            d, i = heapq.heappop(q)
            res.append(points[i])
            K -= 1
        return res