# brute force, get TLE
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []
        for l, r, k in queries:
            charCnt = defaultdict(int)
            for i in range(l, r+1):
                charCnt[s[i]] += 1
            oddCnt = 0
            for c,n in charCnt.items():
                if n % 2 != 0:
                    oddCnt += 1
            res.append(oddCnt//2 <= k)
        return res

# prefix count
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        res = []
        n = len(s)
        charCnt = [[0 for j in range(26)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(26):
                charCnt[i][j] = charCnt[i-1][j]
            charCnt[i][ord(s[i-1])-97] += 1
        # print(charCnt)
        for l, r, k in queries:
            oddCnt = 0
            for c in range(26):
                oddCnt += 1 if (charCnt[r+1][c] - charCnt[l][c]) % 2 != 0 else 0
            # print(oddCnt)
            res.append(oddCnt//2 <= k)
        return res