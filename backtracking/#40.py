class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(pre, target, i):
            if target == 0:
                output.append(pre)
                return
            if i == len(candidates) or candidates[i] > target:
                return
            
            nexti = i+1
            while nexti < len(candidates) and candidates[nexti-1] == candidates[nexti]:
                nexti += 1
            n = 0
            while n <= nexti-i and candidates[i] * n <= target:
                backtrack(pre+[candidates[i]]*n, target-candidates[i]*n, nexti)
                n += 1
        
        candidates.sort()
        output = []
        backtrack([], target, 0)
        
        return output


# same idea, but in a neater way
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(pre, target, i):
            if target == 0:
                output.append(pre)
                return
            if i == len(candidates) or candidates[i] > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                backtrack(pre+[candidates[j]], target-candidates[j], j+1)
        
        candidates.sort()
        output = []
        backtrack([], target, 0)
        
        return output