class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        # find number of unique letters
        maxUnique = len(set(s))
        # check by number of unique letters
        res = 0
        for curUnique in range(1, maxUnique+1):
            counts = [0] * 26
            i, j = 0, 0
            unique, countAtLeastK = 0, 0
            while j < n:
                if unique <= curUnique: # expand sliding window
                    idx = ord(s[j]) - 97
                    if counts[idx] == 0:
                        unique += 1
                    counts[idx] += 1
                    if counts[idx] == k:
                        countAtLeastK += 1
                    j += 1
                else: # shrink sliding window
                    idx = ord(s[i]) - 97
                    if counts[idx] == k:
                        countAtLeastK -= 1
                    counts[idx] -= 1
                    if counts[idx] == 0:
                        unique -= 1
                    i += 1
                if unique == curUnique and unique == countAtLeastK:
                    res = max(res, j- i)
        return res