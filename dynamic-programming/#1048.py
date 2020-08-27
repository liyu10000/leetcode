class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda w: len(w))
        total = len(words)
        count = [1 for _ in range(total)]
        for i in range(1, total):
            for j in range(i):
                if self.predecessor(words[j], words[i]) and count[i] < count[j] + 1:
                    count[i] = count[j] + 1
        # print(count)
        return max(count)
    
    def predecessor(self, word1, word2):
        if len(word2) != len(word1) + 1:
            return False
        for i in range(len(word2)):
            subword = word2[:i] + word2[i+1:]
            if subword == word1:
                return True
        return False