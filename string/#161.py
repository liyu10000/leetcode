class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        sn, tn = len(s), len(t)
        if abs(sn - tn) > 1:
            return False
        if sn <= tn:
            return self.oneCharMore(s, t)
        else:
            return self.oneCharMore(t, s)
        
    def oneCharMore(self, s, t):
        sn, tn = len(s), len(t)
        si, sj = 0, sn-1
        ti, tj = 0, tn-1
        while si < sn:
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                break
        while sj >= si:
            if s[sj] == t[tj]:
                sj -= 1
                tj -= 1
            else:
                break
        return ti == tj