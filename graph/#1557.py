class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inArr = [0] * n
        for i, j in edges:
            inArr[j] += 1
        res = []
        for i in range(n):
            if inArr[i] == 0:
                res.append(i)
        return res