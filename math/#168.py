class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n > 0:
            n, a = divmod(n, 26)
            if a == 0:
                s += 'Z'
                n -= 1
            else:
                s += chr(a + 64)  # 65 for 'A'
        return s[::-1]