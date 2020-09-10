# first trial
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        d = dict()
        for i,c in enumerate(s):
            if c in d:
                m = max(m, len(d))
                keys = list(d.keys())
                for cc in keys:
                    if d[cc] < d[c]:
                        del d[cc]
            d[c] = i
        m = max(m, len(d))
        return m
            

# second trial
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        sub = ''
        for c in s:
            if c not in sub:
                sub += c
            else:
                m = max(m, len(sub))
                sub = sub[sub.index(c)+1:] + c
        m = max(m, len(sub))
        return m

# third trial: using a set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        visited = set()
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if not s[j] in visited:
                visited.add(s[j])
                j += 1
                m = max(m, j - i)
            else:
                visited.remove(s[i])
                i += 1
        return m