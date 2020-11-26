class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        arr = [0 for _ in range(26)]
        for task in tasks:
            arr[ord(task) - ord('A')] += 1
        arr.sort(reverse=True)
        maxlen = arr[0]
        gap = (maxlen - 1) * n
        length = gap + maxlen
        for i in range(1, 26):
            if gap >= arr[i]:
                if arr[i] == maxlen:
                    gap -= (maxlen - 1)
                    length += 1
                else:
                    gap -= arr[i]
            else:
                return len(tasks)
        return length

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        charCnt = defaultdict(int)
        for task in tasks:
            charCnt[task] += 1
        pq = []
        for c,cnt in charCnt.items():
            heapq.heappush(pq, (-cnt, c))
        # print(pq)
        schedules = []
        while pq:
            visited = []
            i = 0
            while i < n+1 and pq:
                cnt, task = heapq.heappop(pq)
                schedules.append(task)
                if cnt < -1:
                    visited.append((cnt+1, task))
                i += 1
            for cnt, task in visited:
                heapq.heappush(pq, (cnt, task))
            schedules += ['idle'] * (n+1-i)
            # print(pq, schedules)
        # remove trailing idles
        while schedules and schedules[-1] == 'idle':
            schedules.pop()
        return len(schedules)