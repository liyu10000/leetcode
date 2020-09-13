# brute force
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows, cols = [], []
        for i in range(m):
            rows.append(sum(mat[i]))
        for j in range(n):
            cols.append(sum([mat[i][j] for i in range(m)]))
        cnt = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] and rows[i] == cols[j] == 1:
                    cnt += 1
        return cnt

