class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        n, p = len(B), len(B[0])
        Aridx, Arval = [], []
        Bcidx, Bcval = [], []
        # get non-zero indices and values of A, by rows
        for i in range(m):
            ridx, rval = [], []
            for j in range(n):
                if A[i][j] != 0:
                    ridx.append(j)
                    rval.append(A[i][j])
            Aridx.append(ridx)
            Arval.append(rval)
        # print(Aridx, Arval)
        # get non-zero indices and values of B, by columns
        for j in range(p):
            cidx, cval = [], []
            for i in range(n):
                if B[i][j] != 0:
                    cidx.append(i)
                    cval.append(B[i][j])
            Bcidx.append(cidx)
            Bcval.append(cval)
        # print(Bcidx, Bcval)
        # perform multiplication
        AB = [[0 for j in range(p)] for i in range(m)]
        for i in range(m):
            for j in range(p):
                ridx, rval = Aridx[i], Arval[i]
                cidx, cval = Bcidx[j], Bcval[j]
                s = 0
                u, v = 0, 0
                while u < len(ridx) and v < len(cidx):
                    if ridx[u] == cidx[v]:
                        s += rval[u] * cval[v]
                        u += 1
                        v += 1
                    elif ridx[u] < cidx[v]:
                        u += 1
                    else:
                        v += 1
                AB[i][j] = s
        return AB