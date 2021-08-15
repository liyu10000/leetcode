# dp solution, get TLE
class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        # find states of palindromic strings between i and j
        dp = [[0 for j in range(n)] for i in range(n)]
        for l in range(1, n+1):
            if l == 1:
                for i in range(n):
                    dp[i][i] = 1
            elif l == 2:
                for i in range(n-1):
                    dp[i][i+1] = 1 if s[i] == s[i+1] else 0
            else:
                for i in range(n-l+1):
                    j = i + l - 1
                    dp[i][j] = 1 if s[i] == s[j] and dp[i+1][j-1] else 0
        # find maximum product
        mp = 0
        for cut in range(n-1):
            # left palindrome
            leftm = 0
            start = cut + 1 if (cut+1) % 2 == 1 else cut
            for l in range(start, 0, -2):
                for i in range(cut-l+2):
                    if dp[i][i+l-1]:
                        leftm = l
                        break
                if leftm > 0:
                    break
            # right palindrome
            rightm = 0
            start = n - cut - 1 if (n-cut-1) % 2 == 1 else n-cut-2
            for l in range(start, 0, -2):
                for i in range(cut+1, n-l+1):
                    if dp[i][i+l-1]:
                        rightm = l
                        break
                if rightm > 0:
                    break
            mp = max(mp, leftm * rightm)
        return mp


# refer this link for more advanced solution:
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/discuss/1389421/Python-O(n)-with-Manacher-explained