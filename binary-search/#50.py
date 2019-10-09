# first try
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

# second try
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        else:
            return self.myPow(x*x, n >> 1) * [1, x][n % 2]