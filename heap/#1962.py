import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        s = sum(piles)
        q = [-p for p in piles]
        heapq.heapify(q)
        for _ in range(k):
            p = heapq.heappop(q)
            delta = (-p) // 2
            s -= delta
            heapq.heappush(q, p+delta)
        return s