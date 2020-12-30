class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for path in paths:
            tokens = path.split()
            p, fs = tokens[0], tokens[1:]
            for f in fs:
                name, content = f[:-1].split('(')
                d[content].append(p + '/' + name)
        res = []
        for content, pfs in d.items():
            if len(pfs) > 1:
                res.append(pfs)
        return res