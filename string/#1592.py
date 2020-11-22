class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        wlen = sum([len(w) for w in words])
        wcnt = len(words)
        tlen = len(text)
        slen = tlen - wlen
        if wcnt == 1:
            return words[0] + ' ' * slen
        else:
            return (' ' * (slen // (wcnt - 1))).join(words) + ' ' * (slen % (wcnt - 1))
        return ''