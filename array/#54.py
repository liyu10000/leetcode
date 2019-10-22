class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        def onion(m1, m2, n1, n2, res):
            if m1 > m2 or n1 > n2:
                return
            if m1 == m2 and n1 == n2:
                res.append(matrix[m1][m2])
            elif m1 == m2:
                res += matrix[m1][n1:n2+1]
            elif n1 == n2:
                res += [matrix[i][n1] for i in range(m1, m2+1)]
            else:
                res += matrix[m1][n1:n2+1]
                res += [matrix[i][n2] for i in range(m1+1, m2)]
                res += matrix[m2][n1:n2+1][::-1]
                res += [matrix[i][n1] for i in range(m1+1, m2)][::-1]
                onion(m1+1, m2-1, n1+1, n2-1, res)
        
        res = []
        onion(0, len(matrix)-1, 0, len(matrix[0])-1, res)
        return res
                