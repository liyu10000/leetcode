# brute force recursive
class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = ''
        i, n = 0, len(S)
        flag = True
        while i < n:
            if i < n-1 and S[i] == S[i+1]:
                flag = False
                i += 2
            else:
                s += S[i]
                i += 1
        if flag:
            return s
        else:
            return self.removeDuplicates(s)

# stack
class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        for c in S:
            if s and s[-1] == c:
                s.pop()
            else:
                s.append(c)
        return ''.join(s)