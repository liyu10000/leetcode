class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        d = defaultdict(int)
        for l, w in rectangles:
            d[min(l, w)] += 1
        k = max(d.keys())
        return d[k]