class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        M = len(a) + len(b)
        acnt = self.charCount(a)
        bcnt = self.charCount(b)
        aforward = self.forward(acnt)
        abackward = self.backward(acnt)
        bforward = self.forward(bcnt)
        bbackward = self.backward(bcnt)
        alessb = M
        for i in range(25):
            alessb = min(alessb, abackward[i+1] + bforward[i])
        blessa = M
        for i in range(1, 26):
            blessa = min(blessa, aforward[i-1] + bbackward[i])
        aequalb = M
        for i in range(26):
            aequalb = min(aequalb, M - acnt[i] - bcnt[i])
        # print(alessb, blessa, aequalb)
        return min(alessb, blessa, aequalb)
    
    def charCount(self, a):
        cnt = [0] * 26
        for c in a:
            cnt[ord(c)-97] += 1
        return cnt
    
    def forward(self, cnt):
        forwardSum = [0] * 26
        forwardSum[0] = cnt[0]
        for i in range(1, 26):
            forwardSum[i] = forwardSum[i-1] + cnt[i]
        return forwardSum
    
    def backward(self, cnt):
        backwardSum = [0] * 26
        backwardSum[-1] = cnt[-1]
        for i in range(24, -1, -1):
            backwardSum[i] = backwardSum[i+1] + cnt[i]
        return backwardSum