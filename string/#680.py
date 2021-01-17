class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
        if i >= j:
            return True
        # remove s[i]
        u, v = i+1, j
        flag1 = True
        while u < v:
            if s[u] != s[v]:
                flag1 = False
            u += 1
            v -= 1
        # remove s[j]
        u, v = i, j-1
        flag2 = True
        while u < v:
            if s[u] != s[v]:
                flag2 = False
            u += 1
            v -= 1
        return flag1 or flag2