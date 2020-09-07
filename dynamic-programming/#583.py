class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        t = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    t[i][j] = t[i-1][j-1] + 1
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        # print(t)
        return n1 + n2 - 2 * t[n1][n2]