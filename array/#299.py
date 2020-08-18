# solution 1
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sd = {}
        gd = {}
        bulls = 0
        len_ = len(secret)
        for i in range(len_):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] not in sd:
                    sd[secret[i]] = 1
                else:
                    sd[secret[i]] += 1
                if guess[i] not in gd:
                    gd[guess[i]] = 1
                else:
                    gd[guess[i]] += 1
        cows = 0
        for c in gd:
            cows += min(gd[c], sd.get(c, 0))
        return str(bulls)+'A'+str(cows)+'B'

# solution 2
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = defaultdict(int)
        for c in secret:
            d[c] += 1
        bulls, cows = 0, 0
        for sc, gc in zip(secret, guess):
            if sc == gc:
                bulls += 1
                d[sc] -= 1
        for sc, gc in zip(secret, guess):
            if sc != gc and d[gc] > 0:
                cows += 1
                d[gc] -= 1
        return str(bulls)+'A'+str(cows)+'B'