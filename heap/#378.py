import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        h = [(matrix[0][0], 0, 0)]
        searched = set()
        while h and k:
            v, i, j = heapq.heappop(h)
            if (i, j) in searched:
                continue
            searched.add((i, j))
            if i < n-1:
                heapq.heappush(h, (matrix[i+1][j], i+1, j))
            if j < n-1:
                heapq.heappush(h, (matrix[i][j+1], i, j+1))
            k -= 1
        return v