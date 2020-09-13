# recursive
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.kth = ''
        self.cnt = 0
        self.buildHappyString(n, k, 0, '')
        return self.kth
        
    def buildHappyString(self, n, k, m, s):
        # print(m, s, self.cnt)
        if m == n:
            self.cnt += 1
            if self.cnt == k:
                self.kth = s
            return
        for c in 'abc':
            if s and s[-1] != c:
                self.buildHappyString(n, k, m+1, s+c)
            elif not s:
                self.buildHappyString(n, k, m+1, c)

