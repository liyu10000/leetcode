# naive solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = len(s) - 1
        while l >= 0 and s[l] == ' ':
            l -= 1
        if l == -1:
            return 0
        i = l - 1
        while i >= 0:
            if s[i] == ' ':
                return l - i
            i -= 1
        if i == -1:
            return l - i
        return 0

