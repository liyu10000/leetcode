class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sCnt = defaultdict(int)
        tCnt = defaultdict(int)
        for c in t:
            tCnt[c] += 1
        i = 0
        resi, resj = -1, len(s)
        for j in range(len(s)):
            sCnt[s[j]] += 1
            while i <= j:
                contain = True
                for c in tCnt:
                    if sCnt[c] < tCnt[c]:
                        contain = False
                        break
                if contain:
                    if j - i < resj - resi:
                        resi = i
                        resj = j
                    sCnt[s[i]] -= 1
                    i += 1
                else:
                    break
        return s[resi:resj+1] if resi != -1 else ''