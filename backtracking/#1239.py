# backtrack, but visit all possible permutations, get TLE
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(idx, s):
            # print(s, carr)
            if idx == nkeys:
                return
            for cur in range(idx, nkeys):
                subs = arr[cur]
                flag = False
                for i,c in enumerate(subs):
                    if carr[ord(c)-a]:
                        flag = True
                        break
                    else:
                        carr[ord(c)-a] = True
                if flag:
                    for j in range(i):
                        carr[ord(subs[j])-a] = False
                else:
                    s += subs
                    self.mlen = max(self.mlen, len(s))
                    backtrack(idx+1, s)
                    s = s[:-len(subs)]
                    for c in subs:
                        carr[ord(c)-a] = False
                    
        n = len(arr)
        a = 97  # ASCII of 'a'
        carr = [False] * 26
        nkeys = len(arr)
        self.mlen = 0
        backtrack(0, '')
        return self.mlen