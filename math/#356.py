class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        y2x = defaultdict(set)
        for x, y in points:
            y2x[y].add(x)
        # check if comes in pairs and determine line
        line = None
        for y, xs in y2x.items():
            n = len(xs)
            xs = list(xs)
            xs.sort()
            i, j = 0, n-1
            while i <= j:
                if line is not None:
                    if line != (xs[i]+xs[j])/2:
                        return False
                else:
                    line = (xs[i]+xs[j]) / 2
                i += 1
                j -= 1
        return True


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        xmin = min(p[0] for p in points)
        xmax = max(p[0] for p in points)
        s = set()
        for p in points:
            s.add(tuple(p))
        for p in s:
            if (xmax + xmin - p[0], p[1]) not in s:
                return False
        return True