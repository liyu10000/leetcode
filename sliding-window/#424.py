from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_l = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            if r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            max_l = max(max_l, r - l + 1)
        return max_l
