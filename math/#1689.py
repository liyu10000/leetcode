class Solution:
    def minPartitions(self, n: str) -> int:
        m = 0
        for c in n:
            m = max(m, int(c))
        return m