# first try
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for i in range(len(s)):
            n += 26 ** (len(s)-i-1) * (ord(s[i]) - 64)  # 65 for 'A'
        return n

# second try
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for c in s:
            n = n * 26 + ord(c) - 64  # 65 for 'A'
        return n