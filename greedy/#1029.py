# use heap
import heapq

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        q = []
        for i,cost in enumerate(costs):
            heapq.heappush(q, [cost[0]-cost[1], i])
        aset = set()
        for i in range(n):
            diff, idx = heapq.heappop(q)
            aset.add(idx)
        s = 0
        for i in range(2*n):
            if i in aset:
                s += costs[i][0]
            else:
                s += costs[i][1]
        return s


# sort
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda c:c[0]-c[1])
        s = 0
        for i in range(n):
            s += costs[i][0] + costs[i+n][1]
        return s