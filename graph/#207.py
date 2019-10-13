# first try
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct graph
        d = defaultdict(list)
        for a, b in prerequisites:
            d[a].append(b)
        
        # check cycle
        def isCycle(a):
            visited[a] = True
            stack[a] = True
            for b in d[a]:
                if not visited[b]:
                    if isCycle(b):
                        return True
                elif stack[b]:
                    return True
            stack[a] = False
            return False
        
        # check all courses
        stack = [False] * numCourses
        visited = [False] * numCourses
        for a in range(numCourses):
            if isCycle(a):
                return False
        return True


# second try
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct graph
        d = defaultdict(list)
        for a, b in prerequisites:
            d[a].append(b)
        
        # check cycle
        def isCycle(a):
            visited.add(a)
            if a not in d:
                return False
            stack.append(a)
            for b in d[a]:
                if b not in visited:
                    if isCycle(b):
                        return True
                elif b in stack:
                    return True
            stack.pop()
            return False
        
        # check all courses
        stack = []
        visited = set()
        for a in d:
            if isCycle(a):
                return False
        return True