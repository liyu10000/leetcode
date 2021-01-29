class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        rows = [[0 for j in range(n)] for i in range(m)]
        xors = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            rows[i][0] = matrix[i][0]
            for j in range(1, n):
                rows[i][j] = rows[i][j-1] ^ matrix[i][j]
        # build xor result matrix
        for j in range(n):
            xors[0][j] = rows[0][j]
        for i in range(1, m):
            for j in range(n):
                xors[i][j] = xors[i-1][j] ^ rows[i][j]
        # get kth largest value
        xors = [xors[i][j] for i in range(m) for j in range(n)]
        xors.sort(reverse=True)
        return xors[k-1]