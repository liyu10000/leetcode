# bfs, get TLE
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        minRefuels = len(stations) + 1
        q = [[0, -startFuel]]
        for station in stations:
            newq = []
            while q:
                refuels, dist = heapq.heappop(q)
                if -dist >= target:
                    minRefuels = min(minRefuels, refuels)
                if -dist >= station[0]:
                    heapq.heappush(newq, [refuels, dist])
                    heapq.heappush(newq, [refuels+1, dist-station[1]])
            q = newq
            # print(q)
        while q:
            refuels, dist = heapq.heappop(q)
            if -dist >= target:
                minRefuels = min(minRefuels, refuels)
        return minRefuels if minRefuels != len(stations)+1 else -1

# dp
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= location:
                    dp[j+1] = max(dp[j+1], dp[j]+capacity)
        # print(dp)
        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1