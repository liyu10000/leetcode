class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0
        cnt2, cnt5 = 0, 0
        for i in range(1, n+1):
            if i % 10 == 0:
                cnt += 1
                i //= 10
            if i % 2 == 0:
                cnt2 += 1
            while i % 5 == 0:
                cnt5 += 1
                i //= 5
        # print(cnt, cnt2, cnt5)
        cnt += min(cnt2, cnt5)
        return cnt

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt5 = 0
        for i in range(5, n+1, 5):
            while i % 5 == 0:
                cnt5 += 1
                i //= 5
        return cnt5