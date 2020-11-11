class Solution:
    digits = set(list('0123456789'))
    
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        i, n = 0, len(s)
        pres = ''
        while i < n:
            if s[i] in self.digits:
                pres = s[:i]
                break
            i += 1
        if i == n:
            return s
        cnt = 0
        while i < n and s[i] in self.digits:
            cnt = cnt * 10 + int(s[i])
            i += 1
        j = i + 1
        b1, b2 = 1, 0
        while j < n and b1 > b2:
            if s[j] == '[':
                b1 += 1
            elif s[j] == ']':
                b2 += 1
            j += 1
        # print(s, i, j)
        mids = self.decodeString(s[i+1:j-1]) * cnt
        if j < n:
            poss = self.decodeString(s[j:])
            return pres + mids + poss
        else:
            return pres + mids