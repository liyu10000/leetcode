class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i, n = 0, len(s)
        for word in words:
            if i == n:
                return True
            if len(word) > n - i:
                return False
            if word != s[i:i+len(word)]:
                return False
            i += len(word)
        return i == n