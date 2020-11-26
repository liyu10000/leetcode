class Solution:    
    def findStrobogrammatic(self, n: int) -> List[str]:
        return self.helper(n, n)
        
    def helper(self, k, n):
        if k == 0:
            return ['']
        if k == 1:
            return ['1', '8', '0']
        if k == 2:
            if n == 2:
                return ["11","69","88","96"]
            else:
                return ["11","69","88","96","00"]
        res = self.helper(k-2, n)
        add = ["11","69","88","96"]
        if k < n:
            add += ["00"]
        newres = []
        for s in res:
            for pre,pos in add:
                newres.append(pre+s+pos)
        return newres