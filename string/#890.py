# two maps, check key-value pairs
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matches = []
        for word in words:
            map1 = {}
            map2 = {}
            flag = True
            for w,p in zip(word, pattern):
                if w in map1 and map1[w] != p:
                    flag = False
                    break
                else:
                    map1[w] = p
                if p in map2 and map2[p] != w:
                    flag = False
                    break
                else:
                    map2[p] = w
            if flag:
                matches.append(word)
        return matches

# count frequency and change matching keys
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p = self.toPattern(pattern)
        matches = []
        for word in words:
            w = self.toPattern(word)
            if p == w:
                matches.append(word)
        return matches
    
    def toPattern(self, word):
        m = {}
        curr = 0
        for c in word:
            if not c in m:
                curr += 1
                m[c] = curr
        p = ''.join([chr(m[c]+96) for c in word])
        return p