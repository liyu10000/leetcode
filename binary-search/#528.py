import random

class Solution:

    def __init__(self, w: List[int]):
        l = len(w)
        s = [0 for i in range(l)]
        s[0] = w[0]
        for i in range(1, l):
            s[i] = s[i-1] + w[i]
        self.l = l
        self.s = s        

    def pickIndex(self) -> int:
        a = random.random() * self.s[-1]
        i = self.search(a)
        # print(a, i)
        return i

    def search(self, a):
        if a <= self.s[0]:
            return 0
        i, j = 0, self.l
        while i < j:
            m = (i + j) // 2
            if self.s[m] >= a:
                j = m
            else:
                i = m + 1
        return i