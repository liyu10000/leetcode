# use built-in functions
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        words = words[::-1]
        return ' '.join(words)

# don't pass, but the idea is correct
class Solution:
    def reverseWords(self, s: str) -> str:
        # reverse string
        s = s[::-1]
        n = len(s)
        i, j = 0, 0
        while j < n:
            # find each word
            while i < n and s[i] == ' ':
                i += 1
            j = i
            while j < n and s[j] != ' ':
                j += 1
            # reverse word
            u, v = i, j-1
            while u < v:
                s[u], s[v] = s[v], s[u]
                u += 1
                v -= 1
            i = j
        # remove extra spaces
        trim(s)
        return s