class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps
        l = [[power(x), x] for x in range(lo, hi+1)]
        l.sort()
        # print(l)
        return l[k-1][1]