class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = 0, 0
        i = 0
        plugin = False
        while i < len(intervals):
            if newInterval[0] <= intervals[i][1]:
                if newInterval[1] < intervals[i][0]:
                    left = i
                    right = i
                    plugin = True
                    a, b = newInterval
                    break
                a = min(newInterval[0], intervals[i][0])
                b = max(newInterval[1], intervals[i][1])
                left = i
                while i+1 < len(intervals) and b >= intervals[i+1][0]:
                    b = max(b, intervals[i+1][1])
                    i += 1
                right = i + 1
                plugin = True
                break
            i += 1
        return intervals[:left] + ([[a, b]] if plugin else []) + intervals[right:] + ([newInterval] if not plugin else [])