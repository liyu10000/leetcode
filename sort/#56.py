from operator import itemgetter

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals = sorted(intervals, key=lambda x:x[0])
        intervals = sorted(intervals, key=itemgetter(0))
        res = []
        i = 0
        while i < len(intervals):
            a, b = intervals[i]
            while i+1 < len(intervals) and intervals[i+1][0] <= b:
                b = max(b, intervals[i+1][1])
                i += 1
            res.append([a, b])
            i += 1
        return res