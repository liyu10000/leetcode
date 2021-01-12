class DisjointSet:
    def __init__(self, N):
        self.parents = list(range(N))
    
    def find(self, i):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        self.parents[self.find(i)] = self.find(j)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DisjointSet(n)
        components = n
        for i, j in edges:
            ir = dsu.find(i)
            jr = dsu.find(j)
            if ir != jr:
                dsu.parents[ir] = jr
                components -= 1
        return components