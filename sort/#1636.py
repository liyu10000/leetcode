class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cntd = defaultdict(int)
        for n in nums:
            cntd[n] += 1
        ordd = defaultdict(list)
        for n,c in cntd.items():
            ordd[c].append(n)
        for c in ordd:
            ns = ordd[c]
            ns.sort(reverse=True)
        res = []
        cs = list(ordd.keys())
        cs.sort()
        for c in cs:
            ns = ordd[c]
            for n in ns:
                res += [n] * c
        return res