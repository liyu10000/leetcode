# recursion with memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        memo = defaultdict(list)
        
        def helper(s):
            if not s:
                return [[]]
            if s in memo:
                return memo[s]
            for endIndex in range(len(s), 0, -1):
                word = s[:endIndex]
                if word in words:
                    for sent in helper(s[endIndex:]):
                        memo[s].append([word]+sent)
            return memo[s]
        
        helper(s)
        return [' '.join(words) for words in memo[s]]