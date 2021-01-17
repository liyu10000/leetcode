class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lens = [len(w) for w in words]
        i, j = 0, 0
        n = len(words)
        texts = []
        while j < n:
            l = 0 # prime word length
            while j < n and l + lens[j] + j - i <= maxWidth:
                l += lens[j]
                j += 1
            
            m = j - i # number of words
            l = maxWidth - l # number of spaces
            if j < n:
                if m > 1:
                    s, r = l // (m - 1), l % (m - 1) # average space, remaining space
                    line = words[i]
                    for k in range(i+1, j):
                        line += ' ' * (s + (1 if r > 0 else 0)) + words[k]
                        r -= 1
                else:
                    line = words[i] + ' ' * l
                # print(i, j, s, r)
            else:
                line = ' '.join(words[i:]) + ' ' * (l - m + 1)
            texts.append(line)
            i = j
        return texts