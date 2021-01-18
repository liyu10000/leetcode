# sort intervals and use heap to keep max item
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = [[interval.start, interval.end] for employee in schedule for interval in employee]
        intervals.sort(key=lambda i:i[0])
        print(intervals)
        n = len(intervals)
        free = []
        q = [-intervals[0][1]]
        for i in range(1, n):
            if intervals[i][0] > -q[0]:
                free.append([-heapq.heappop(q), intervals[i][0]])
            heapq.heappush(q, -intervals[i][1])
        return [Interval(i[0], i[1]) for i in free]

# sort intervals
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = [[interval.start, interval.end] for employee in schedule for interval in employee]
        intervals.sort(key=lambda i:i[0])
        # print(intervals)
        n = len(intervals)
        free = []
        last = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] > last:
                free.append(Interval(last, intervals[i][0]))
            last = max(last, intervals[i][1])
        return free