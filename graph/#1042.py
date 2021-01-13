class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # build graph
        graph = [[] for _ in range(n)]
        for i,j in paths:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        # paint color greedily
        colors = [0] * n
        for i in range(n):
            colors[i] = ({1,2,3,4}-{colors[j] for j in graph[i]}).pop()
        return colors