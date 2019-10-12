class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combine(pre, target, i, res):
            if target == 0:
                res.append(pre)
                return
            if i == len(candidates) or candidates[i] > target:
                return
            
            nexti = i+1
            while nexti < len(candidates) and candidates[nexti-1] == candidates[nexti]:
                nexti += 1
            n = 0
            while n <= nexti-i and candidates[i] * n <= target:
                combine(pre+[candidates[i]]*n, target-candidates[i]*n, nexti, res)
                n += 1
        
        candidates.sort()
        res = []
        combine([], target, 0, res)
        
        return res