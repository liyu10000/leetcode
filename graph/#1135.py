# minimum spanning tree: Kruskal's algorithm
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
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # sort edges by costs
        connections.sort(key=lambda e:e[2])
        # build graph
        cost = 0
        components = N
        dsu = DisjointSet(N+1)
        for i,j,c in connections:
            ir = dsu.find(i)
            jr = dsu.find(j)
            # print(i, j, ir, jr)
            if ir != jr:
                dsu.parents[ir] = jr
                cost += c
                components -= 1
        return cost if components == 1 else -1