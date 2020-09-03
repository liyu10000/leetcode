# first trial
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':'abc', '3':'def', '4':'ghi',
                   '5':'jkl', '6':'mno', '7':'pqrs',
                   '8':'tuv', '9':'wxyz'}
        res = []
        for d in digits:
            if not res:
                res = list(mapping[d])
            else:
                newres = []
                for c in mapping[d]:
                    for r in res:
                        newres.append(r+c)
                res = newres
                del newres
        return res

# second trial: recursive approach
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':'abc', '3':'def', '4':'ghi',
                   '5':'jkl', '6':'mno', '7':'pqrs',
                   '8':'tuv', '9':'wxyz'}
        if not digits:
            return []
        res = []
        def generate(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
            else:
                for c in mapping[digits[i]]:
                    generate(i+1, curr+c)
        generate(0, '')
        return res

# third trial: backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl',
                        '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.res = []
        self.backtrack(digits, 0, len(digits), [])
        return self.res
        
    def backtrack(self, digits, i, n, curr):
        if i == n:
            self.res += curr
            return
        s = self.mapping[digits[i]]
        if not curr:
            self.backtrack(digits, i+1, n, list(s))
        else:
            for c in s:
                self.backtrack(digits, i+1, n, [item+c for item in curr])