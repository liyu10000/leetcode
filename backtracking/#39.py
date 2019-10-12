# first try
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combine(pre, target, i, res):
            if target == 0:
                res.append(pre)
                return
            for ii in range(i, len(candidates)):
                if target - candidates[ii] >= 0:
                    combine(pre+[candidates[ii]], target-candidates[ii], ii, res)
        
        candidates.sort()
        res = []
        combine([], target, 0, res)
        
        return res

# second try
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def combine(pre, target, i, res):
            if target == 0:
                res.append(pre)
                return
            if i == len(candidates) or candidates[i] > target:
                return
            
            n = 0
            while candidates[i] * n <= target:
                combine(pre+[candidates[i]]*n, target-candidates[i]*n, i+1, res)
                n += 1
                    
        candidates.sort()
        res = []
        combine([], target, 0, res)
        
        return res