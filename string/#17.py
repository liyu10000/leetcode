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