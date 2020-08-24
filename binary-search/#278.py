class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return r