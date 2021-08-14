class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        if n <= 2:
            return s
        res = s[:2]
        for i in range(2, n):
            if s[i] == res[-2] and s[i] == res[-1]:
                continue
            else:
                res += s[i]
        return res