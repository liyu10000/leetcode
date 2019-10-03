class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        if l <= 1:
            return s
        length = 1
        i = 0
        res = s[0]
        while i < l - length // 2:
            left, right = i, i
            while left > 0 and s[left] == s[left-1]:
                left -= 1
            while right < l-1 and s[right] == s[right+1]:
                right += 1
            while left >= 0 and right < l and s[left] == s[right]:
                left -= 1
                right += 1
            if (right - left - 1) > length:
                length = right - left - 1
                res = s[left+1:right]
            i += 1
        return res