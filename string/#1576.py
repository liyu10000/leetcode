class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        res = ''
        i, j = 0, 0
        allc = 'abcdefghijklmnopqrstuvwxyz'
        while j < n:
            # find where ? starts
            while i < n and s[i] != '?':
                res += s[i]
                i += 1
            # find where ? ends (s[j] != ?)
            j = i
            while j < n and s[j] == '?':
                j += 1
            # get the two chars to avoid
            if i == 0 and j == n:
                h, t = ' ', ' '
            elif i == 0:
                h, t = ' ', s[j]
            elif j == n:
                h, t = s[i-1], ' '
            else:
                h, t = s[i-1], s[j]
            # get the two chars to replace
            p1, p2 = 'a', 'b'
            for c in allc:
                if c != h and c != t:
                    p1 = c
                    break
            for c in allc:
                if c != h and c != t and c != p1:
                    p2 = c
                    break
            # fill in chars
            for k in range(i, j):
                if k % 2 == 0:
                    res += p1
                else:
                    res += p2
            i = j
        return res