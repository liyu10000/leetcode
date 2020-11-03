class Solution:
    def isHappy(self, n: int) -> bool:
        found = set()
        while n != 1:
            if n in found:
                return False
            found.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return True