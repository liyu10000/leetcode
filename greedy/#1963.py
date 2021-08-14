class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        m = 0
        for c in s:
            if c == '[':
                imbalance -= 1
            else:
                imbalance += 1
            m = max(m, imbalance)
        return (m + 1) // 2
            