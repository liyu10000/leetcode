class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, op = 0, '+'
        for i,c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            if not c.isdigit() and c != ' ' or i == len(s)-1:
                if op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                elif op == '/':
                    top = stack.pop()
                    curres = top // num if top >= 0 else - (-top // num)
                    stack.append(curres)
                elif op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                op = c
                num = 0
        # print(stack)
        res = sum(stack)
        return res