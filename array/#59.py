class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def onion(m1, m2, n1, n2, val, res):
            if m1 > m2 or n1 > n2:
                return
            if m1 == m2 and n1 == n2:
                res[m1][n1] = val
            elif m1 == m2:
                res[m1][n1:n2+1] = range(val, val+n2+1-n1)
            elif n1 == n2:
                for i in range(m1, m2+1):
                    res[i][n1] = val
                    val += 1
            else:
                for i in range(n1, n2):
                    res[m1][i] = val
                    val += 1
                for i in range(m1, m2):
                    res[i][n2] = val
                    val += 1
                for i in range(n2, n1, -1):
                    res[m2][i] = val
                    val += 1
                for i in range(m2, m1, -1):
                    res[i][n1] = val
                    val += 1
                onion(m1+1, m2-1, n1+1, n2-1, val, res)
        
        res = [[0] * n for i in range(n)]
        onion(0, n-1, 0, n-1, 1, res)
        return res