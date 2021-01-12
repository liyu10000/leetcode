# brute force
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        check = [0] * (N+1)
        for i,j in trust:
            check[j] += 1
        trust = {tuple(t) for t in trust}
        for i in range(1,N+1):
            if check[i] == N-1:
                for j in range(1,N+1):
                    if (i,j) in trust:
                        return -1
                return i
        return -1

# indegree and outdegree arrays
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        inArr = [0] * (N+1)
        outArr = [0] * (N+1)
        for i, j in trust:
            inArr[j] += 1
            outArr[i] = 1
        for i in range(1, N+1):
            if inArr[i] == N-1 and outArr[i] == 0:
                return i
        return -1

# use one array, record indegree - outdegree
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N-1:
            return -1
        check = [0] * (N+1)
        for i,j in trust:
            check[j] += 1
            check[i] -= 1
        for i in range(1,N+1):
            if check[i] == N-1:
                return i
        return -1