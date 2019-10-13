# solution posted on LeetCode
from collections import defaultdict

class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []


# cumbersome solution
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # construct graph
        d = defaultdict(list)
        for a, b in prerequisites:
            d[a].append(b)
            
        if self.hasCycle(numCourses, d):
            return []
        else:
            return self.findRoute(numCourses, d)
        
    # check cycle
    def hasCycle(self, numCourses, d):
        def isCycle(i):
            visited[i] = True
            if not i in d:
                return False
            stack[i] = True
            for j in d[i]:
                if not visited[j]:
                    if isCycle(j):
                        return True
                elif stack[j]:
                    return True
            stack[i] = False
            return False
        
        stack = [False] * numCourses
        visited = [False] * numCourses
        for i in range(numCourses):
            if not visited[i] and isCycle(i):
                return True
        return False
    
    # find topological route
    def findRoute(self, numCourses, d):
        def findRouteUtil(i):
            visited[i] = True
            if i in d:
                for j in d[i]:
                    if not visited[j]:
                        findRouteUtil(j)
            stack.append(i)
        
        stack = []
        visited = [False] * numCourses
        for i in range(numCourses):
            if not visited[i]:
                findRouteUtil(i)
        return stack