class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        charMap = ' abcdefghijklmnopqrstuvwxyz'
        maxK = 26 * n
        incArr = [maxK] * n
        incArr[-1] = 0
        for i in range(n-2, -1, -1):
            incArr[i] = incArr[i+1] + 26
            if k < incArr[i]:
                break
        # print(incArr)
        s = ''
        for i in range(n):
            if k <= incArr[i]:
                s += 'a'
                k -= 1
            else:
                idx = k - incArr[i]
                k -= idx
                s += charMap[idx]
        return s