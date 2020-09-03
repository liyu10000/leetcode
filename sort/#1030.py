from collections import defaultdict
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(R):
            for j in range(C):
                d[abs(i-r0)+abs(j-c0)].append([i,j])
        res = []
        keys = list(d.keys())
        keys.sort()
        for k in keys:
            res += d[k]
        return res


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        def dist(point):
            pi, pj = point
            return abs(pi - r0) + abs(pj - c0)

        points = [(i, j) for i in range(R) for j in range(C)]
        return sorted(points, key=dist)