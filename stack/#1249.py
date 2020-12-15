class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lstack, rstack = [], []
        cnt = 0
        for i,c in enumerate(s):
            if c == '(':
                cnt += 1
                lstack.append(i)
            elif c == ')':
                cnt -= 1
                rstack.append(i)
            while cnt < 0:
                rstack.pop()
                cnt += 1
        while cnt > 0:
            lstack.pop()
            cnt -= 1
        iset = set(lstack+rstack)
        res = [c for i,c in enumerate(s) if i in iset or (c != '(' and c != ')')]
        return ''.join(res)