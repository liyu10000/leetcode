class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * len(edges)
        
        def find(x):
            if parent[x] == 0: 
                return x 
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty: 
                return False 
            parent[rootx] = rooty 
            return True 

        for x,y in edges: 
            if not union(x-1,y-1):
                return x,y 