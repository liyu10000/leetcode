class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        arr1 = self.cnt(s)
        arr2 = self.cnt(s[::-1])[::-1]
        # print(arr1, arr2)
        samecnt = 0
        for i in range(n-1):
            if arr1[i] == arr2[i+1]:
                samecnt += 1
        return samecnt
    
    def cnt(self, s):
        n = len(s)
        arr = [1 for _ in range(n)]
        cnt = 1
        unique = {s[0]}
        for i in range(1, n):
            if s[i] in unique:
                arr[i] = cnt
            else:
                unique.add(s[i])
                cnt += 1
                arr[i] = cnt
        return arr