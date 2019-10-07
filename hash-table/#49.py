# first try
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            ss = tuple(sorted(s))
            if not ss in d:
                d[ss] = []
            d[ss].append(s)
        r = []
        for k,v in d.items():
            r.append(v)
        return r

# second try
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            ss = tuple(sorted(s))
            if not ss in d:
                d[ss] = [s]
            else:
                d[ss].append(s)
        return list(d.values())