class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        num, sign = 0, 1
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num
                num, sign = 0, 1
            elif c == '-':
                res += sign * num
                num, sign = 0, -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res += sign * num
        return res