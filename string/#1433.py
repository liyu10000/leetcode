class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1)) 
        s2 = ''.join(sorted(s2)) 
        return self.canBreak(s1, s2) or self.canBreak(s2, s1)
    
    def canBreak(self, s1, s2):
        for c1,c2 in zip(s1, s2):
            if c1 > c2:
                return False
        return True