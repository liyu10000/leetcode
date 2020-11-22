class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        unique = set()
        self.cnt = 0
        self.backtrack(s, n, 0, unique)
        return self.cnt
        
    def backtrack(self, s, n, i, unique):
        if i == n:
            self.cnt = max(self.cnt, len(unique))
            return
        for j in range(i, n):
            if not s[i:j+1] in unique:
                unique.add(s[i:j+1])
                self.backtrack(s, n, j+1, unique)
                unique.remove(s[i:j+1])
                
        # # greedy
        # n = len(s)
        # d = set()
        # i, j = 0, 0
        # while j < n:
        #     if not s[i:j+1] in d:
        #         d.add(s[i:j+1])
        #         i, j = j + 1, j + 1
        #     else:
        #         while j < n:
        #             j += 1
        #             if not s[i:j+1] in d:
        #                 d.add(s[i:j+1])
        #                 i, j = j + 1, j + 1
        #                 break
        # return len(d)
        
        # # dp
        # n = len(s)
        # dp = [[0] * n for _ in range(n)]
        # for l in range(1, n+1):
        #     if l == 1:
        #         for i in range(n):
        #             dp[i][i] = 1
        #     elif l == 2:
        #         for i in range(n-1):
        #             dp[i][i+1] = 2 if s[i] != s[i+1] else 1
        #     else:
        #         for i in range(n-l+1):
        #             pass