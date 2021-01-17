class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        n = len(A)
        a, b = [], []
        duplicates = set()
        hasDup = False
        for i in range(n):
            if A[i] in duplicates:
                hasDup = True
            else:
                duplicates.add(A[i])
            if A[i] != B[i]:
                a.append(A[i])
                b.append(B[i])
            if len(a) > 2:
                return False
        return (len(a) == 2 and a[0] == b[1] and a[1] == b[0]) or (len(a) == 0 and hasDup)