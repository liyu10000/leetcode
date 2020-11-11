# brute force: check overlaps at each time stamp, get TLE
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        m1 = min(min([i[0] for i in intervals]), min([i[1] for i in intervals]))
        m2 = max(max([i[0] for i in intervals]), max([i[1] for i in intervals]))
        # print(m1, m2)
        cnt = [0] * (m2 - m1 + 1)
        for i in intervals:
            for t in range(i[0], i[1]):
                cnt[t-m1] += 1
        # print(cnt)
        return max(cnt)

# using heap queue with greedy
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i:i[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])
        for i in intervals[1:]:
            if i[0] >= heap[0]:  # greedy happens here
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])
        return len(heap)