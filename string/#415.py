class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        num1 = num1[::-1]
        num2 = num2[::-1]
        c = 0
        s = ''
        for n1, n2 in zip(num1, num2):
            c += int(n1) + int(n2)
            n = c % 10
            c = c // 10
            s += str(n)
        i, j = len(num2), len(num1)
        for k in range(i, j):
            c += int(num1[k])
            n = c % 10
            c = c // 10
            s += str(n)
        if c:
            s += str(c)
        return s[::-1]