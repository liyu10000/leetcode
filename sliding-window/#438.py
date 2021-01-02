# two pointers
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        scounts = [0] * 26 # char counts of moving window of s
        pcounts = [0] * 26 # char counts of p
        ns, np = len(s), len(p)
        for c in p:
            pcounts[ord(c)-97] += 1
        res = []
        i, j = 0, 0
        while j < ns:
            idxj = ord(s[j]) - 97
            scounts[idxj] += 1
            while scounts[idxj] > pcounts[idxj]:
                scounts[ord(s[i])-97] -= 1
                i += 1
            if j - i + 1 == np:
                res.append(i)
                scounts[ord(s[i])-97] -= 1
                i += 1
            j += 1
            # print(i, j, scounts)
        return res

