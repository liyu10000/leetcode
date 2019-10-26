class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        status = [False] * len(s)
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and (j == len(s) or status[j]):
                    status[i] = True
                    break
        return status[0]