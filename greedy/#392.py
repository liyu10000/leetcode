class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = -1
        for c in s:
            i = t.find(c, i+1)
            if i == -1:
                return False
        return True