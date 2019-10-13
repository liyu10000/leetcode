class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for x,y in tickets:
            graph[x].append(y)
            
        L = len(tickets)
        res = ["JFK"]
        def dfs(port):
            if len(res) == L + 1:
                return True
            for nex in sorted(graph[port]):
                graph[port].remove(nex)
                res.append(nex)
                if dfs(nex):
                    return True
                else:
                    graph[port].append(nex)
                    res.pop()
            return False
        
        dfs("JFK")
        return res