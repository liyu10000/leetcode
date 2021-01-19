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

# dp, more understandable
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        # t[i][j] means dist between word1[:n1] and word2[:n2]
        t = [[0 for j in range(n2+1)] for i in range(n1+1)]
        for i in range(n1+1):
            t[i][0] = i
        for j in range(n2+1):
            t[0][j] = j
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    t[i][j] = t[i-1][j-1]
                else:
                    t[i][j] = min(t[i-1][j]+1, t[i][j-1]+1, t[i-1][j-1]+2)
        # print(t)
        return t[n1][n2]
