class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # construct graph and count connections for each city
        graph = [[0 for j in range(n)] for i in range(n)]
        connections = [[i, 0] for i in range(n)]
        for i, j in roads:
            graph[i][j] = graph[j][i] = 1
            connections[i] += 1
            connections[j] += 1
        # find maximum network rank
        mrank = 0
        for i in range(n-1):
            for j in range(i+1, n):
                mrank = max(mrank, connections[i]+connections[j]+(-1 if graph[i][j] else 0))
        return mrank