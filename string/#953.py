class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {c:i for i,c in enumerate(order)}
        orderMap[' '] = -1 # for null char
        n = len(words)
        maxl = max(map(len, words))
        keep = True
        for p in range(maxl):
            if keep:
                keep = False
                for i in range(n-1):
                    c1 = words[i][p] if p < len(words[i]) else ' '
                    c2 = words[i+1][p] if p < len(words[i+1]) else ' '
                    if orderMap[c1] == orderMap[c2]:
                        keep = True
                    elif orderMap[c1] > orderMap[c2]:
                        return False
        return True