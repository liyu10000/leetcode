# O(nlogn), get TLE
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        d = defaultdict(list)
        for i,h in enumerate(heights):
            d[h].append(i)
        keys = list(d.keys())
        keys.sort()
        # print(keys, d)
        n = len(heights)
        area = 0
        prevh = -1
        for h in keys:
            # print(area, prevh, h, d)
            if prevh == -1:
                area = n * h
            else:
                ps = d[prevh]
                for i,p in enumerate(ps):
                    if i == 0 and p != 0:
                        area = max(area, p*h)
                    if i == len(ps) - 1 and p != n - 1:
                        area = max(area, (n-p-1)*h)
                    if i > 0:
                        area = max(area, (p - ps[i-1] - 1) * h)
                newps = d[h] + d[prevh]
                newps.sort()
                d[h] = newps
                del d[prevh]
            prevh = h
        return area