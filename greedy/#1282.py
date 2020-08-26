class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        d = defaultdict(list)
        for i,g in enumerate(groupSizes):
            d[g].append(i)
            if len(d[g]) == g:
                res.append(d.pop(g))
        return res
