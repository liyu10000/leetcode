# BFS, track all paths
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        
        # bfs
        q = [[0]]
        while q:
            newq = []
            for path in q:
                end = path[-1]
                if end == n-1:
                    paths.append(path)
                else:
                    for nxt in graph[end]:
                        newq.append(path+[nxt])
            q = newq
        return paths

# also BFS, pop one item instead of one level each time
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        
        # bfs
        q = [[0]]
        while q:
            path = q.pop() # should be q.pop(0) to be real bfs
            end = path[-1]
            if end == n-1:
                paths.append(path)
            else:
                for nxt in graph[end]:
                    q.append(path+[nxt])
        return paths

# backtracking
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        
        # backtrack
        def backtrack(i, path):
            if i == n-1:
                paths.append(path)
                return
            for nxt in graph[i]:
                backtrack(nxt, path+[nxt])
        
        backtrack(0, [0])
        return paths