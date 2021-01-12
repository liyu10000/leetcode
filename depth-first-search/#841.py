class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        N = len(rooms)
        opens = 0
        visited = [0] * N
        
        def dfs(i):
            nonlocal opens
            opens += 1
            # print(opens, N, i)
            if opens >= N:
                return
            visited[i] = 1
            for j in rooms[i]:
                if not visited[j]:
                    dfs(j)
        
        dfs(0)
        return opens >= N