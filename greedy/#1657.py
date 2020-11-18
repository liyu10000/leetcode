class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        chars1, counts1 = self.count(word1)
        chars2, counts2 = self.count(word2)
        if len(chars1) != len(chars2) or len(counts1) != len(counts2):
            return False
        for c1, c2 in zip(chars1, chars2):
            if c1 != c2:
                return False
        for c1, c2 in zip(counts1, counts2):
            if c1 != c2:
                return False
        return True
    
    def count(self, word):
        d = defaultdict(int)
        for c in word:
            d[c] += 1
        chars = list(d.keys())
        chars.sort()
        counts = list(d.values())
        counts.sort()
        return chars, counts