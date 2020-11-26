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

# BFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n
        setID = 1
        for i in range(n):
            if not visited[i]:
                visited[i] = setID
                # BFS
                students = [j for j in range(n) if j != i and M[i][j]]
                while students:
                    newstudents = []
                    for s in students:
                        if not visited[s]:
                            visited[s] = setID
                            for j in range(n):
                                if j != s and j != i and M[s][j]:
                                    newstudents.append(j)
                    students = newstudents
                setID += 1
                # print(setID, visited)
        return setID - 1

# DFS
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n
        setID = 1
        for i in range(n):
            if not visited[i]:
                self.dfs(M, visited, n, i, setID)
                setID += 1
                # print(setID, visited)
        return setID - 1
    
    def dfs(self, M, visited, n, i, setID):
        visited[i] = setID
        for j in range(n):
            if not visited[j] and M[i][j]:
                self.dfs(M, visited, n, j, setID)