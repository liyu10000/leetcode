class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for cpdomain in cpdomains:
            c, domain = cpdomain.split(' ')
            c = int(c)
            tokens = domain.split('.')
            for i in range(len(tokens)):
                d['.'.join(tokens[i:])] += c
        res = []
        for domain, c in d.items():
            res.append(str(c) + ' ' + domain)
        return res