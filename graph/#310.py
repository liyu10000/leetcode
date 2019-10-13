class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # build graph
        adj_list = {i:[] for i in range(n)}
        
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        # find leaf nodes and trim
        leaves = [i for i in adj_list if len(adj_list[i]) == 1]
        leaves_tobe = []
        while leaves:
            for i in leaves:
                for nb in adj_list[i]:
                    adj_list[nb].remove(i)
                    if len(adj_list[nb]) == 1:
                        leaves_tobe.append(nb)
            if not leaves_tobe:
                break
            leaves, leaves_tobe = leaves_tobe, []
            
        return leaves