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

# dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        m = 0
        sub = ""
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if j == i:
                    dp[i][j] = 1
                elif j == i + 1:
                    dp[i][j] = 1 if s[i] == s[j] else 0
                else:
                    dp[i][j] = 1 if s[i] == s[j] and dp[i+1][j-1] else 0
                if dp[i][j] and j - i + 1 > m:
                    m = j - i + 1
                    sub = s[i:j+1]
        # print(dp)
        return sub