class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m, n = len(rooms), len(rooms[0])
        INF = 2147483647
        q = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
        # bfs
        while q:
            newq = []
            for i, j in q:
                for u, v in [(i-1,j), (i,j+1), (i+1,j), (i,j-1)]:
                    if 0 <= u < m and 0 <= v < n and rooms[u][v] == INF:
                        rooms[u][v] = rooms[i][j] + 1
                        newq.append((u, v))
            q = newq