# time limit exceeded
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        arr = [0, 1, 2] + [0] * (n - 2)
        for i in range(3, n+1):
            arr[i] = arr[i-2] + arr[i-1]
        return arr[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        n1, n2 = 1, 2
        for i in range(3, n+1):
            n3 = n1 + n2
            n1, n2 = n2, n3
        return n3
