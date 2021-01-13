class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        marks = [0] * n # 0: not visited, 1: visited but search not finished, 2: search finished
        
        def dfs(i):
            marks[i] = 1
            for j in graph[i]:
                if marks[j] == 1:
                    return True
                if marks[j] == 0 and dfs(j):
                    return True
            marks[i] = 2
            return False
        
        circles = 0
        for i in range(n):
            if marks[i] == 0 and dfs(i):
                circles += 1
        safe = [i for i in range(n) if marks[i] == 2]
        # print(marks)
        # print('# circles', circles)
        return safe