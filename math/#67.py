class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        c = ''
        i, j = len(a) - 1, len(b) - 1
        while i != -1 and j != -1:
            carry += 1 if a[i] == '1' else 0
            carry += 1 if b[j] == '1' else 0
            c += '1' if carry % 2 != 0 else '0'
            carry //= 2
            i -= 1
            j -= 1
        if j != -1:
            i = j
            a = b
        while i != -1:
            carry += 1 if a[i] == '1' else 0
            c += '1' if carry % 2 != 0 else '0'
            carry //= 2
            i -= 1
        if carry:
            c += '1'
        return c[::-1]