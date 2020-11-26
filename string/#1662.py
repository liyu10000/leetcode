class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        citer1 = self.charIter(word1)
        citer2 = self.charIter(word2)
        for c1, c2 in zip(citer1, citer2):
            # print(c1, c2)
            if c1 != c2:
                return False
        return not c1 and not c2
    
    def charIter(self, words):
        for word in words:
            for c in word:
                yield c
        yield ''