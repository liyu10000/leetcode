class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        i, l = 0, len(s)
        map1 = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        map2 = {'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
        while i < l:
            if s[i:i+2] in map2:
                num += map2[s[i:i+2]]
                i += 2
                continue
            if s[i] in map1:
                num += map1[s[i]]
                i += 1
                continue
        return num