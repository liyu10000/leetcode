class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # construct graph
        graph = dict()
        for (a, b), val in zip(equations, values):
            if not a in graph:
                graph[a] = {}
            if not b in graph:
                graph[b] = {}
            graph[a][b] = val
            graph[b][a] = 1.0/val
        
        # find path and do divisions step by step
        def findPath(a, b, val):
            if not a in graph or not b in graph:
                return False, -1.0
            if a == b:
                return True, 1.0
            if b in graph[a]:
                return True, val*graph[a][b]
            
            visited.add(a)
            for cand in graph[a]:
                if not cand in visited:
                    isPath, val_next = findPath(cand, b, val*graph[a][cand])
                    if isPath:
                        return True, val_next
                        
            visited.remove(a)
            return False, -1.0
        
        # evaluate queries
        res = []
        for a, b in queries:
            visited = set()
            _, val = findPath(a, b, 1.0)
            res.append(val)
            
        return res