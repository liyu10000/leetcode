class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        res = [[0] * n, [0] * n]
        for i in range(n):
            if colsum[i] == 2:
                res[0][i] = res[1][i] = 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    res[0][i] = 1
                    upper -= 1
                else:
                    res[1][i] = 1
                    lower -= 1
            if upper < 0 or lower < 0:
                return []
        return res if upper == 0 and lower == 0 else []