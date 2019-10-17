class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        n = len(M)
        visited = [False] * n
        count = 0
        
        def findCycle(i):
            visited[i] = True
            for j in range(n):
                if not visited[j] and M[i][j]:
                    findCycle(j)
                    
        for i in range(n):
            if not visited[i]:
                count += 1
                findCycle(i)
  
        return count
