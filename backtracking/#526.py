# naive backtracking
class Solution:
    def countArrangement(self, N: int) -> int:
        self.cnt = 0
        
        def backtrack(i):
            if i == N+1:
                self.cnt += 1
                return
            for n in range(1, N+1):
                if not visited[n] and (n % i == 0 or i % n == 0):
                    visited[n] = True
                    backtrack(i+1)
                    visited[n] = False
        
        visited = [False] * (N + 1)
        backtrack(1)
        return self.cnt

# backtracking with memorization
class Solution:
    def countArrangement(self, N: int) -> int:
        self.cnt = 0
        dmap = defaultdict(set)
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i % j == 0 or j % i == 0:
                    dmap[i].add(j)
        
        def backtrack(i):
            if i == N+1:
                self.cnt += 1
                return
            for n in range(1, N+1):
                if not visited[n] and n in dmap[i]:
                    visited[n] = True
                    backtrack(i+1)
                    visited[n] = False
        
        visited = [False] * (N + 1)
        backtrack(1)
        return self.cnt

